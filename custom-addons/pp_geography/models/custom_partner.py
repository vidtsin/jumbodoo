from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    district_id = fields.Many2one('pp.district',
                                  string='District',
                                  index=True,
                                  ondelete='restrict')
    amphur_id = fields.Many2one('pp.amphur',
                                string='Amphur',
                                index=True,
                                ondelete='restrict')
    province_id = fields.Many2one('pp.province',
                                  string='Province',
                                  index=True,
                                  ondelete='restrict')

    @api.onchange('district_id')
    def onchange_district_id(self):
        if self.district_id:
            self.amphur_id = self.district_id.amphur_id.id
            self.province_id = self.district_id.province_id.id
            self.street2 = f"{self.district_id.name} {self.district_id.amphur_id.name}"
            self.city = self.district_id.province_id.name
            zip = self.env['pp.zipcode'].search([('district_id', '=', self.district_id.id),
                                                 ('amphur_id', '=', self.district_id.amphur_id.id),
                                                 ('province_id', '=', self.district_id.province_id.id)])
            if zip:
                self.zip = zip.name

            self.country_id = 217  # Thailand Country Code
