#  Copyright (c) 2019.
#  Author: Jakkrit S.
#  Company: PPSmartProduct Co., Ltd.

import logging

from odoo import fields, models, api
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

UPDATE_PARTNER_FIELDS = ['firstname', 'lastname', 'user_id', 'address_home_id']


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _get_name(self, lastname, firstname):
        return self.env['res.partner']._get_computed_name(lastname, firstname)

    @api.onchange('firstname', 'lastname')
    def _onchange_firstname_lastname(self):
        if self.firstname or self.lastname:
            self.name = self._get_name(self.lastname, self.firstname)

    firstname = fields.Char()
    lastname = fields.Char()

