# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['openacademy.teachers']
        return http.request.render('openacademy.index', {
            'teachers': Teachers.search([])
        })

    @http.route('/academy/<model("openacademy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('openacademy.biography', {
            'person': teacher
        })

