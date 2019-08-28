# -*- coding: utf-8 -*-
from odoo import http

# class PpHr(http.Controller):
#     @http.route('/pp_hr/pp_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pp_hr/pp_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pp_hr.listing', {
#             'root': '/pp_hr/pp_hr',
#             'objects': http.request.env['pp_hr.pp_hr'].search([]),
#         })

#     @http.route('/pp_hr/pp_hr/objects/<model("pp_hr.pp_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pp_hr.object', {
#             'object': obj
#         })