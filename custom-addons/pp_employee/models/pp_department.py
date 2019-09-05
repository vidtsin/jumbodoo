# -*- coding: utf-8 -*-

#  Copyright (c) 2019.
#  Author: Jakkrit S.
#  Company: PPSmartProduct Co., Ltd.

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date


class PPDepartment(models.Model):
    _name = 'pp.department'
    _description = 'pp company department model for jumbo industry'
    _inherit = ['hr.department', 'mail.thread']

