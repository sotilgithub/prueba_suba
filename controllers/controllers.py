# -*- coding: utf-8 -*-
# from odoo import http


# class BasicoGenerado8(http.Controller):
#     @http.route('/basico_generado8/basico_generado8/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/basico_generado8/basico_generado8/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('basico_generado8.listing', {
#             'root': '/basico_generado8/basico_generado8',
#             'objects': http.request.env['basico_generado8.basico_generado8'].search([]),
#         })

#     @http.route('/basico_generado8/basico_generado8/objects/<model("basico_generado8.basico_generado8"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('basico_generado8.object', {
#             'object': obj
#         })
