from odoo import _, api, fields, models, tools

class StudentRendezvous(models.Model):

    _name = 'student.rendezvous'
    _description = 'Rendez-vous'
    _rec_name = 'student_id'

    date_debut = fields.Date()
    date_fin = fields.Date()
    student_id = fields.Many2one(
        'school.student',
        string='Elève',
    )
    description = fields.Char()