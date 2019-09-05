# -*- coding: utf-8 -*-

#  copyright (c) 2019.
#  author: jakkrit s.
#  company: ppsmartproduct co., ltd.

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date


class PPEmployeeCategory(models.Model):
    _name = 'pp.employee.category'
    _description = 'pp employee category model for jumbo industry'
    _inherit = ['hr.employee.category', 'mail.thread']

