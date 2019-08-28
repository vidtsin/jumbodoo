# -*- coding: utf-8 -*-
from odoo import http

# class PpsmartGeography(http.Controller):
#     @http.route('/ppsmart_geography/ppsmart_geography/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ppsmart_geography/ppsmart_geography/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ppsmart_geography.listing', {
#             'root': '/ppsmart_geography/ppsmart_geography',
#             'objects': http.request.env['ppsmart_geography.ppsmart_geography'].search([]),
#         })

#     @http.route('/ppsmart_geography/ppsmart_geography/objects/<model("ppsmart_geography.ppsmart_geography"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ppsmart_geography.object', {
#             'object': obj
#         })