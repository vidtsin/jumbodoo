# -*- coding: utf-8 -*-
from odoo import http

# class Jumbo(http.Controller):
#     @http.route('/jumbo/jumbo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jumbo/jumbo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jumbo.listing', {
#             'root': '/jumbo/jumbo',
#             'objects': http.request.env['jumbo.jumbo'].search([]),
#         })

#     @http.route('/jumbo/jumbo/objects/<model("jumbo.jumbo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jumbo.object', {
#             'object': obj
#         })