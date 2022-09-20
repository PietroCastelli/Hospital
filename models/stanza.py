from odoo import models, fields

class Stanza(models.Model):
    _name = 'hospital.stanza'
    _description = 'hospital.stanza'
    name = fields.Char(string="Nome stanza")
    reparto_id = fields.Many2one("hospital.reparto",
        "reparto id")



