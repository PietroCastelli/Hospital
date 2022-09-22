from odoo import models, fields


class Hospitalization(models.Model):
    _name = 'hospital.hospitalization'
    _description = 'hospital.hospitalization'
    name = fields.Char(string="name")
    note = fields.Html(string="testo")
    paziente_id = fields.Many2one("res.partner", domain="[('isPatient', '=',True)]")
    doctor_id = fields.Many2one("res.partner",domain="[('isDoctor', '=',True)]")
    date_hospitalization_in = fields.Datetime(string="Check in")
    date_hospitalization_out = fields.Datetime(string="Check out")
    disease = fields.Char(string="Disease")
    room_id = fields.Many2one("hospital.room")

