# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
                                 ('islam', 'Islam')], translate=True)
    jumbo_employee_id = fields.Char(string='Employee Badge ID', translate=True)  # รหัสพนักงาน
