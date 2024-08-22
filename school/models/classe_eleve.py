from odoo import _, api, fields, models, tools

class StudentClass(models.Model):

    _name = 'student.class'
    _description = 'Classe'

    name = fields.Char(string="Nom de classe", required=True)

    student_ids = fields.One2many('school.student', 'class_id')