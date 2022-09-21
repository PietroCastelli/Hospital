from odoo import models, fields

class Reparto(models.Model):
    _name = 'hospital.reparto'
    _description = 'hospital.reparto'
    name = fields.Char(string="Name")
    stanze_count = fields.Integer(string="Stanze", compute="compute_stanze_count")
    stanza_ids = fields.One2many("hospital.stanza",
        "reparto_id",
        "stanze ids")

    def compute_stanze_count(self):
        for stanze in self:
            #result = self.env['hospital.reparto'].search_count([('stanza_ids', '=', stanze.stanza_ids)])
            stanze.stanze_count = len(stanze.stanza_ids)
    def action_go_stanze(self):
        return
"""
len(self.revision_ids)
<button name="action_go_to_notes" icon="fa-file-o" type="object">
                <field name="notes_count" widget="statinfo"/>
             </button>
def compute_notes_count(self):
    for record in self:
        result = self.env['note.note'].search_count([('partner_id', '=', record.id)])
        record.notes_count = result


def action_go_to_notes(self):
    action = self.env.ref('note.action_note_note').read()[0]
    action['domain'] = [('id', 'in', self.note_ids.ids)]
    action['context'] = {
        'default_partner_id': self.note_ids.partner_id.id,
        'readonly_partner_id': True,
    }
    return action
    notes_count = fields.Integer(string="Note", compute="compute_notes_count")
    """


