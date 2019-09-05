# -*- coding: utf-8 -*-
from odoo import http

# class Custom-addons/ppEmployee(http.Controller):
#     @http.route('/custom-addons/pp_employee/custom-addons/pp_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/pp_employee/custom-addons/pp_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/pp_employee.listing', {
#             'root': '/custom-addons/pp_employee/custom-addons/pp_employee',
#             'objects': http.request.env['custom-addons/pp_employee.custom-addons/pp_employee'].search([]),
#         })

#     @http.route('/custom-addons/pp_employee/custom-addons/pp_employee/objects/<model("custom-addons/pp_employee.custom-addons/pp_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/pp_employee.object', {
#             'object': obj
#         })