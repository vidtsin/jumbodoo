# Copyright 2017 Vicent Cubells - <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import common
from odoo.exceptions import UserError


class TestHrExpenseInvoice(common.SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestHrExpenseInvoice, cls).setUpClass()

        partner = cls.env['res.partner'].create({
            'name': 'Test partner',
            'supplier': True,
        })
        employee_home = cls.env['res.partner'].create({
            'name': 'Employee Home Address',
        })
        receivable = cls.env.ref('account.data_account_type_receivable').id
        expenses = cls.env.ref('account.data_account_type_expenses').id
        invoice_account = cls.env['account.account'].search(
            [('user_type_id', '=', receivable)], limit=1).id
        invoice_line_account = cls.env['account.account'].search(
            [('user_type_id', '=', expenses)], limit=1).id
        product = cls.env['product.product'].create({
            'name': 'Product test',
            'type': 'service',
        })
        employee = cls.env['hr.employee'].create({
            'name': 'Employee A',
            'address_home_id': employee_home.id,
        })
        cls.invoice = cls.env['account.invoice'].create({
            'partner_id': partner.id,
            'account_id': invoice_account,
            'type': 'in_invoice',
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'quantity': 1.0,
                'price_unit': 100.0,
                'name': 'product that cost 100',
                'account_id': invoice_line_account,
            })]
        })
        cls.invoice2 = cls.invoice.copy({
            'invoice_line_ids': [(0, 0, {
                'product_id': product.id,
                'quantity': 1.0,
                'price_unit': 100.0,
                'name': 'product that cost 100',
                'account_id': invoice_line_account,
            })]
        })
        cls.sheet = cls.env['hr.expense.sheet'].create({
            'name': 'Test expense sheet',
            'employee_id': employee.id,
        })
        cls.expense = cls.env['hr.expense'].create({
            'name': 'Expense test',
            'employee_id': employee.id,
            'product_id': product.id,
            'unit_amount': 50.0,
        })
        cls.expense2 = cls.expense.copy()
        cls.expense3 = cls.expense.copy()

    def test_0_hr_test_no_invoice(self):
        # There is not expense lines in sheet
        self.assertEqual(len(self.sheet.expense_line_ids), 0)
        # We add an expense
        self.sheet.expense_line_ids = [(6, 0, [self.expense.id])]
        self.assertEqual(len(self.sheet.expense_line_ids), 1)
        self.assertAlmostEqual(self.expense.total_amount, 50.0)
        # We approve sheet, no invoice
        self.sheet.approve_expense_sheets()
        self.assertEqual(self.sheet.state, 'approve')
        self.assertFalse(self.sheet.account_move_id)
        # We post journal entries
        self.sheet.action_sheet_move_create()
        self.assertEqual(self.sheet.state, 'post')
        self.assertTrue(self.sheet.account_move_id)

    def test_1_hr_test_invoice(self):
        # There is no expense lines in sheet
        self.assertEqual(len(self.sheet.expense_line_ids), 0)
        # We add an expense
        self.sheet.expense_line_ids = [(6, 0, [self.expense.id])]
        self.assertEqual(len(self.sheet.expense_line_ids), 1)
        # We add invoice to expense
        self.invoice.action_invoice_open()
        self.expense.invoice_id = self.invoice.id
        self.expense.onchange_invoice_id()
        self.assertAlmostEqual(self.expense.total_amount, 100.0)
        # We approve sheet
        self.sheet.approve_expense_sheets()
        self.assertEqual(self.sheet.state, 'approve')
        self.assertFalse(self.sheet.account_move_id)
        self.assertEqual(self.invoice.state, 'open')
        # We post journal entries
        self.sheet.action_sheet_move_create()
        self.assertEqual(self.sheet.state, 'post')
        self.assertTrue(self.sheet.account_move_id)
        # Invoice is now paid
        self.assertEqual(self.invoice.state, 'paid')

    def test_2_hr_test_multi_invoices(self):
        # There is no expense lines in sheet
        self.assertEqual(len(self.sheet.expense_line_ids), 0)
        # We add 2 expenses
        self.sheet.expense_line_ids = [(6, 0, [self.expense.id,
                                               self.expense2.id])]
        self.assertEqual(len(self.sheet.expense_line_ids), 2)
        # We add invoices to expenses
        self.invoice.action_invoice_open()
        self.invoice2.action_invoice_open()
        self.expense.invoice_id = self.invoice.id
        self.expense2.invoice_id = self.invoice2.id
        self.expense.onchange_invoice_id()
        self.expense2.onchange_invoice_id()
        self.assertAlmostEqual(self.expense.total_amount, 100.0)
        self.assertAlmostEqual(self.expense2.total_amount, 100.0)
        # We approve sheet
        self.sheet.approve_expense_sheets()
        self.assertEqual(self.sheet.state, 'approve')
        self.assertFalse(self.sheet.account_move_id)
        self.assertEqual(self.invoice.state, 'open')
        # We post journal entries
        self.sheet.action_sheet_move_create()
        self.assertEqual(self.sheet.state, 'post')
        self.assertTrue(self.sheet.account_move_id)
        # Invoice is now paid
        self.assertEqual(self.invoice.state, 'paid')

    def test_3_hr_test_expense_create_invoice(self):
        # There is no expense lines in sheet
        self.assertEqual(len(self.sheet.expense_line_ids), 0)
        # We add 3 expenses
        self.sheet.expense_line_ids = [(6, 0, [self.expense.id,
                                               self.expense2.id,
                                               self.expense3.id,
                                               ])]
        self.assertEqual(len(self.sheet.expense_line_ids), 3)
        # We create 1st invoice from expense 1, 2
        ctx = {'active_id': self.sheet.id,
               'active_ids': [self.sheet.id],
               'active_model': 'hr.expense.sheet'}
        vals = {'expense_ids': [(6, 0, [self.expense.id, self.expense2.id])]}
        Wizard = self.env['hr.expense.create.invoice']
        with self.assertRaises(UserError):
            wizard = Wizard.with_context(ctx).create(vals)
        self.sheet.approve_expense_sheets()
        wizard = Wizard.with_context(ctx).create(vals)
        invoice = wizard.create_invoice()
        # A new invoice is created
        self.assertEqual([invoice.id],
                         self.sheet.expense_line_ids.mapped('invoice_id').ids)
        self.assertEqual(self.sheet.invoice_count, 1)
        res = self.sheet.action_view_invoices()
        # Click on View Invoice button link to the correct invoice
        self.assertEqual(res['res_id'], invoice.id)

        # We create 2nd invoice from expense 3
        ctx = {'active_id': self.sheet.id,
               'active_ids': [self.sheet.id],
               'active_model': 'hr.expense.sheet'}
        vals = {'expense_ids': [(6, 0, [self.expense3.id])]}
        Wizard = self.env['hr.expense.create.invoice']
        self.sheet.approve_expense_sheets()
        wizard = Wizard.with_context(ctx).create(vals)
        invoice2 = wizard.create_invoice()
        # Now there are 2 invoices
        self.assertItemsEqual(
            [invoice.id, invoice2.id],
            self.sheet.expense_line_ids.mapped('invoice_id').ids)
        self.sheet.invalidate_cache()  # Make sure invoice_count is recalc
        self.assertEqual(self.sheet.invoice_count, 2)
        res = self.sheet.action_view_invoices()
        # Click on View Invoice button link to the correct invoice
        self.assertEqual(res['view_mode'], 'tree,form')
