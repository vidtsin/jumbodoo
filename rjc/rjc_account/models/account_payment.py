# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    value_date = fields.Date(
        states={'draft': [('readonly', False)]},
        readonly=True,
    )
    payment_ref = fields.Char(
        states={'draft': [('readonly', False)]},
        readonly=True,
        )
    cheque_no = fields.Char(
        string='Cheque No.'
    )
    validate_by = fields.Many2one(
        comodel_name='res.users',
        readonly=True,
    )
    notes = fields.Text(
        string='Internal Notes',
        states={'draft': [('readonly', False)]},
        readonly=True,
        )

    @api.constrains('value_date')
    def _check_value_date(self):
        if not self.value_date:
            raise ValidationError(_("Please select date in Value Date."))

    @api.multi
    def post(self):
        for payment in self:
            payment.validate_by = self.env.user.id
        return super(AccountPayment, self).post()


class AccountRegisterPayments(models.TransientModel):
    _inherit = 'account.register.payments'

    payment_ref = fields.Char()
    notes = fields.Text(
        string='Internal Notes',
    )
    value_date = fields.Date(
        required=True,
    )
    cheque_no = fields.Char(
        string='Cheque No.',
    )

    @api.multi
    def _prepare_payment_vals(self, invoices):
        values = super()._prepare_payment_vals(invoices)
        values['payment_ref'] = self.payment_ref
        values['notes'] = self.notes
        values['cheque_no'] = self.cheque_no
        values['value_date'] = self.value_date
        return values
