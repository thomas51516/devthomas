from odoo import _, api, fields, models, tools
from datetime import date

class SchoolStudent(models.Model):

    _name = 'school.student'
    _inherit= ['mail.thread','mail.activity.mixin']
    _description = 'Student'

    name = fields.Char(string="Nom de famille", required=True, 
    track_visibility='onchange'
    )
    birth_date = fields.Date(string='Date de naissance', 
    track_visibility='onchange',
     default=date.today())
    photo = fields.Binary(string="Photo")
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est est ancien élève")
    sexe = fields.Selection([
        ('Masculin', 'Masculin'),
        ('Féminin','Féminin'),
        ('Autre','Autre')
    ], 
    track_visibility='onchange'
    )
    age = fields.Integer(string="Age", 
    track_visibility='onchange',
     store=True, compute="_compute_age")
    note = fields.Float(string="Note")
    class_id = fields.Many2one(
        'student.class',
        string='Classe',
    )

    course_ids = fields.Many2many('school.course', string="Cours")
    note_ids = fields.One2many('student.note', 'student_id')

    email = fields.Char(string="E-mail", 
    track_visibility='onchange'
    )
    phone = fields.Char(string="Téléphone", 
    track_visibility='onchange'
    )

    progression = fields.Float(string="Progression", default=23)
    course_time = fields.Float(string="Heure de cours")

    priority = fields.Selection([
        ('moyen', 'Moyen'),
        ('normal','Norml'),
        ('eleve','Elevé'),
        ('Tres eleve','Très elevé')
    ], default="eleve")

    state = fields.Selection([
        ('preinscription', 'Préinscription'),
        ('inscription','Inscription'),
        ('abandonne','Abandonné'),
        ('exclu','Exclu')
    ], default='preinscription')

    def compute_preinscription(self):
        self.state = 'preinscription'

    def compute_excul(self):
        self.state = 'exclu'


    def compute_abandonne(self):
        self.state = 'abandonne'

    def compute_inscription(self):
        self.state = 'inscription'

    def compute_progress(self):
        self.progression +=  5

    @api.onchange('birth_date')
    @api.depends('birth_date','age')
    def _compute_age(self):
        age = 0
        if self.birth_date:
            today = date.today()
            birth_date = self.birth_date
            age = today.year - birth_date.year
        self.age = age