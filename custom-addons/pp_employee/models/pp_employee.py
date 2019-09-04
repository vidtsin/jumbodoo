#  Copyright (c) 2019.
#  Author: Jakkrit S.
#  Company: PPSmartProduct Co., Ltd.

from odoo import fields, models, _


class PPHREmployee(models.Model):
    _name = 'pp hr employee'
    _description = 'PP HR Employee for Jumbo Industry'
    _inherit = 'hr.employee'


