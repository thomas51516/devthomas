from odoo import _, api, fields, models, tools
from datetime import date

class SchoolStudent(models.Model):

    _name = 'school.student'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Student'

    name = fields.Char(string="Nom de famille", required=True, 
    track_visibility='always'
    )
    birth_date = fields.Date(string='Date de naissance', default=date.today())
    photo = fields.Binary(string="Photo")
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est est ancien élève")
    sexe = fields.Selection([
        ('Masculin', 'Masculin'),
        ('Féminin','Féminin'),
        ('Autre','Autre')
    ])
    age = fields.Integer(string="Age", compute='_compute_age')
    note = fields.Float(string="Note")
    class_id = fields.Many2one(
        'student.class',
        string='Classe',
    )

    progession = fields.Float(string="Progression", default=1)

    course_ids = fields.Many2many('school.course', string="Cours")
    note_ids = fields.One2many('student.note', 'student_id')

    priority = fields.Selection([
        ('1', 'Faible'),
        ('2','Moyen'),
        ('3','Normal'),
        ('4','Elevé'),
        ('5','Très élevé')
    ], 
    track_visibility='onchange'
    )

    state = fields.Selection([
        ('preinscription', 'Préinscription'),
        ('inscription', 'Inscription'),
        ('abandonne','Abandonné'),
    ], default="preinscription", 
    track_visibility='onchange'
    )

    def abandonner(self):
        for el in self:
            el.state = 'abandonne'

    def inscrire(self):
        for el in self:
            el.write({
                'state':'inscription'
            })

    def compute_progression(self):
        self.progession += 5


    def compute_pro(self):
        self.progession -=5

    @api.onchange('birth_date')
    def _compute_age(self):
        for el in self:
            age  = 0
            if el.birth_date:
                today = date.today()
                birth_date = el.birth_date
                age = today.year - birth_date.year
            el.age = age