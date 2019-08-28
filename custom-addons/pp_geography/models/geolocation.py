# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PPGeography(models.Model):
    _name = 'pp.geography'
    _inherit = ['mail.thread']
    _description = "PPsmart Geolocation for Thailand city names"

    name = fields.Char(string='Name',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    code = fields.Char(string='Code',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')

    active = fields.Boolean(default=True)


class PPProvince(models.Model):
    _name = "pp.province"
    _inherit = ['mail.thread']
    _description = "Province"
    _order = 'code, name'

    name = fields.Char(string='Name',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    code = fields.Char(string='Code',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    geo_id = fields.Many2one('pp.geography',
                             string='GeographicID',
                             required=True,
                             copy=False,
                             index=True,
                             track_visibitily='onchange')

    active = fields.Boolean(default=True)


class PPAmphur(models.Model):
    _name = "pp.amphur"
    _inherit = ['mail.thread']
    _description = "Amphur"
    _order = 'code, name'

    name = fields.Char(string='Name',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    code = fields.Char(string='Code',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    geo_id = fields.Many2one('pp.geography',
                             string='GeographicID',
                             required=True,
                             copy=False,
                             index=True,
                             track_visibitily='onchange')
    province_id = fields.Many2one('pp.province',
                                  string='Province',
                                  copy=False,
                                  index=True,
                                  track_visibitily='onchange')

    active = fields.Boolean(default=True)


class PPDistrict(models.Model):
    _name = "pp.district"
    _inherit = ['mail.thread']
    _description = "District"
    _order = 'code, name'

    name = fields.Char(string='Name',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    code = fields.Char(string='Code',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    geo_id = fields.Many2one('pp.geography',
                             string='GeographicID',
                             required=True,
                             copy=False,
                             index=True,
                             track_visibitily='onchange')
    province_id = fields.Many2one('pp.province',
                                  string='Province',
                                  copy=False,
                                  index=True,
                                  track_visibitily='onchange')

    amphur_id = fields.Many2one('pp.amphur',
                                string='Amphur',
                                copy=False,
                                index=True,
                                track_visibitily='onchange')

    active = fields.Boolean(default=True)

    @api.multi
    @api.depends('name', 'code', 'geo_id', 'province_id', 'amphur_id')
    def name_get(self):
        res = []
        for record in self:
            name = record.name
            if self._context.get('show_fully', False):
                name = f"{record.name}/{record.amphur_id.name}/{record.province_id.name}"
            res.append((record.id, name))
        return res


class PPZipcode(models.Model):
    _name = "pp.zipcode"
    _inherit = ['mail.thread']
    _description = "Zipcode"
    _order = 'name'

    name = fields.Char(string='Name',
                       required=True,
                       copy=False,
                       index=True,
                       track_visibitily='onchange')
    province_id = fields.Many2one('pp.province',
                                  string='Province',
                                  required=True,
                                  copy=False,
                                  index=True,
                                  track_visibitily='onchange')
    amphur_id = fields.Many2one('pp.amphur',
                                string='Amphur',
                                copy=False,
                                index=True,
                                track_visibitily='onchange')
    district_id = fields.Many2one('pp.district',
                                  string='District',
                                  copy=False,
                                  index=True,
                                  track_visibitily='onchange')

    active = fields.Boolean(default=True)
