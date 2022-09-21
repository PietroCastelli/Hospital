# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = ["res.partner"]
    isPatient = fields.Boolean("Patient Active?", default=False)
    isDoctor = fields.Boolean("Doctor Active?", default=False)