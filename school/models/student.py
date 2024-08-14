from odoo import _, api, fields, models, tools

class SchoolStudent(models.Model):

    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string="Nom de famille")
    birth_date = fields.Date(string='Date de naissance')
    photo = fields.Binary(string="Photo")
    description = fields.Html()