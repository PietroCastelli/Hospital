from odoo import models, fields

class room(models.Model):
    _name = 'hospital.room'
    _description = 'hospital.room'
    name = fields.Char(string="Name room")
    department_id = fields.Many2one("hospital.department",
        "department id")




