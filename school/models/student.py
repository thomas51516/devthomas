from odoo import _, api, fields, models, tools
from datetime import date
class SchoolStudent(models.Model):

    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Nom de famille")
    birth_date = fields.Date(string='Date de naissance', default=date.today())
    photo = fields.Binary(string="Photo")
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est est ancien élève")
    sexe = fields.Selection([
        ('Masculin', 'Masculin'),
        ('Féminin','Féminin'),
        ('Autre','Autre')
    ])
    age = fields.Integer(string="Age")
    note = fields.Float(string="Note")