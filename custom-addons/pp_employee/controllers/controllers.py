# -*- coding: utf-8 -*-
from odoo import http

# class PpEmployee(http.Controller):
#     @http.route('/pp_employee/pp_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pp_employee/pp_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pp_employee.listing', {
#             'root': '/pp_employee/pp_employee',
#             'objects': http.request.env['pp_employee.pp_employee'].search([]),
#         })

#     @http.route('/pp_employee/pp_employee/objects/<model("pp_employee.pp_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pp_employee.object', {
#             'object': obj
#         })