#  Copyright (c) 2019.
#  Author: Jakkrit S.
#  Company: PPSmartProduct Co., Ltd.

from odoo import fields, models, _


class PPEmployee(models.Model):
    _name = 'pp.hr.employee'
    _description = 'PPSmart HR Employee for Jumbo Industry'
    _inherit = 'hr.employee'



