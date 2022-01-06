# -*- coding: utf-8 -*-
# from odoo import http


# class Covid-19(http.Controller):
#     @http.route('/covid-19/covid-19/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/covid-19/covid-19/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('covid-19.listing', {
#             'root': '/covid-19/covid-19',
#             'objects': http.request.env['covid-19.covid-19'].search([]),
#         })

#     @http.route('/covid-19/covid-19/objects/<model("covid-19.covid-19"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('covid-19.object', {
#             'object': obj
#         })
