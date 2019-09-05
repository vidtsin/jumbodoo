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
    _inherit = ['hr.employee', 'mail.thread']

    religion = fields.Selection([('buddhism', 'Buddhism'),
                                 ('christian', 'Christian'),
                                 ('islam', 'Islam'),
                                 ('none', 'No Religion')], translate=True)

    employee_badge_id = fields.Char(string='Employee Badge ID', translate=True)  # รหัสพนักงาน

    salutation = fields.Selection([('mr', 'Mr.'),
                                   ('ms', 'Ms.'),
                                   ('mrs', 'Mrs.'),
                                   ('dr', 'Dr.')], translate=True)

    english_name = fields.Char(string='Name in English',
                               translate=True,
                               placeholder='Your name in English (for Thai Localization)')

    taxpayer_id = fields.Char(string='Tax Payer ID', translate=True)

    financial_institution = fields.Selection([('kbank', 'Kasikorn'),
                                              ('ktb', 'Krung Thai'),
                                              ('ksr', 'Krung Sri'),
                                              ('gsb', 'Government Savings Bank')], translate=True)

    identification_expiry = fields.Date(string="ID's Expiry Date", translate=True)
    identification_issued = fields.Date(string="ID's Issued Date", translate=True)

    ethnicity_ids = fields.Many2one('res.country', string='Ethnicity')

    province_ids = fields.Many2one('pp.province',
                                   string='Hometown',
                                   translate=True,
                                   index=True,
                                   ondelete='restrict')

    military_status = fields.Selection([('na', 'Not Applicable'),
                                        ('passed', 'Passed'),
                                        ('postponed', 'Postponed'),
                                        ('veteran', 'Veteran'),
                                        ('reserved', 'Reserved'),
                                        ('active_duty', 'Active Duty')],
                                       translate=True,
                                       default='na')

    blood_type = fields.Selection([('a', 'A'),
                                   ('b', 'B'),
                                   ('o', 'O'),
                                   ('ab', 'AB'),
                                   ('na', 'NA')],
                                  translate=True,
                                  default='na')

    weight = fields.Float(string='Weight (kg.)', translate=True)

    height = fields.Float(string='Height (cm.)', translate=True)

    age = fields.Char(string="employee's age",
                      compute='_get_age',
                      translate=True)

    mother_name = fields.Char("Employee's mother's name", translate=True, default='Not Disclosed')
    father_name = fields.Char("Employee's father's name", translate=True, default='Not Disclosed')

    mother_occupation = fields.Char("Employee's mother's work", translate=True, default='Not Disclosed')
    father_occupation = fields.Char("Employee's father's work", translate=True, default='Not Disclosed')

    emergency_contact_address = fields.Char("Emergency's contact address", translate=True)
    emergency_contact_phone = fields.Char("Emergency's contact phone", translate=True)

    spouse_name = fields.Char("Spouse's Name", translate=True, default='Not Disclosed')
    spouse_work_address = fields.Char("Spouse's Work Address", translate=True, default='Not Disclosed')
    spouse_occupation = fields.Char("Spouse's Occupation", translate=True, default='Not Disclosed')
    spouse_job_title = fields.Char("Spouse's Job Title", translate=True, default='Not Disclosed')
    spouse_phone = fields.Char("Spouse's Phone", translate=True)
    spouse_taxpayer_id = fields.Char("Spouse's Taxpayer ID", translate=True)
    spouse_tax_district_name = fields.Char("Spouse Tax District", translate=True)
    spouse_tax_province_ids = fields.Many2one("pp.province",
                                              string='Tax Form Sent to Province',
                                              translate=True,
                                              index=True,
                                              ondelete='restrict')
    spouse_identification_type = fields.Char("Spouse's Identification Type", translate=True)
    spouse_identification_id = fields.Char("Spouse's Identification Number", translate=True)
    spouse_current_work_status = fields.Char("Spouse's Work Status", translate=True)
    spouse_current_out_of_job_date = fields.Date("Spouse Out-of-Job Date", translate=True)
    spouse_current_out_of_job_reason = fields.Char("Spouse Out-of-Job Reason", translate=True)

    employee_type = fields.Selection([('0', 'Full Time'), ('1', 'Daily'), ('2', 'Per Piece')],
                                     string="Employee Type",
                                     default='1',
                                     translate=True)

    employee_payrate = fields.Integer(string='Pay Rate', translate=True, default=0)

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
