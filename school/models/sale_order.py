from odoo import _, api, fields, models, tools 
from odoo.exceptions import UserError, ValidationError



class SaleOrder(models.Model):

    _inherit = 'sale.order'

    comfirmed_user_id = fields.Many2one(
        'res.users',
        string='Utilisateur confirmé',
    )

    def action_quotation_send(self):
        if not self.comfirmed_user_id:
            raise UserError(_('Impossible d\'envoyer le mail si l\'utilisateur n\'est pas renseigné !!!'))
        

        return None