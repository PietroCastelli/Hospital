# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = ["res.partner"]
    isPatient = fields.Boolean("Patient Active?", default=False)
    isDoctor = fields.Boolean("Doctor Active?", default=False)





# class prova(models.Model):
#     _name = 'prova.prova'
#     _description = 'prova.prova'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
