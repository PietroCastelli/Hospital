from odoo import models, fields

class department(models.Model):
    _name = 'hospital.department'
    _description = 'hospital.department'
    name = fields.Char(string="Name")
    rooms_count = fields.Integer(string="rooms", compute="compute_rooms_count")
    room_ids = fields.One2many("hospital.room",
        "department_id",
        "rooms ids")

    def compute_rooms_count(self):
        for rooms in self:
            rooms.rooms_count = len(rooms.room_ids)
    def action_go_rooms(self):
        print()
        return


