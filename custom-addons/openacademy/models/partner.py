# -*- coding: utf-8 -*-

from odoo import fields, models


# instructors and attendees
class Partner(models.Model):
    _inherit = 'res.partner'

    # add column
    instructor = fields.Boolean("Instructor", default=False)
    session_ids = fields.Many2many('openacademy.session',
                                   string='Attended Sessions',
                                   readonly=True)
