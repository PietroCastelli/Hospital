from odoo import models, fields

class Reparto(models.Model):
    _name = 'hospital.reparto'
    _description = 'hospital.reparto'
    name = fields.Char(string="Name")
    stanza_ids = fields.One2many("hospital.stanza",
        "reparto_id",
        "stanze ids")



