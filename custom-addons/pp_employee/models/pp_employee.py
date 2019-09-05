# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date


# class custom-addons/pp_employee(models.Model):
#     _name = 'custom-addons/pp_employee.custom-addons/pp_employee'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class PPEmployee(models.Model):
    _name = 'pp.employee'
    _description = 'PP Employee Model for Jumbo Industry'
    _inherit = 'hr.employee'

    religion = fields.Selection([('buddhism', 'Buddhism'),
                                 ('christian', 'Christian'),
                                 ('islam', 'Islam'),
                                 ('none', 'No Religion')], translate=True)

    employee_badge_id = fields.Char(string='Employee Badge ID', translate=True)  # รหัสพนักงาน

    salutation = fields.Selection([('mr', 'Mr.'),
                                   ('ms', 'Ms.'),
                                   ('mrs', 'Mrs.'),
                                   ('dr', 'Dr.')], translate=True)

    english_name = fields.Char(string='Name in English', translate=True)

    taxpayer_id = fields.Char(string='Tax Payer ID', translate=True)

    financial_institution = fields.Selection([('kbank', 'Kasikorn'),
                                              ('ktb', 'Krung Thai'),
                                              ('ksr', 'Krung Sri'),
                                              ('gsb', 'Government Savings Bank')], translate=True)

    age = fields.Char(string="employee's age",
                      compute='_get_age',
                      translate=True)

    @api.depends('birthday')
    def _get_age(self):
        for record in self:
            if record.birthday:
                year = relativedelta(date.today(), record.birthday).years
                month = relativedelta(date.today(), record.birthday).months
                day = relativedelta(date.today(), record.birthday).days
                if year > 1:
                    year = _("%s years") % year
                else:
                    year = _("%s year") % year

                if month > 1:
                    month = _("%s months") % month
                else:
                    month = _("%s month") % month

                if day > 1:
                    day = _("%s days") % day
                else:
                    day = _("%s day") % day

                record.age = year + ' ' + month + ' ' + day
            else:
                record.age = 'N/A'



