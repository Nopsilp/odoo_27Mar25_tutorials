"""

"""
from odoo import models, fields

class CustomRecord(models.Model):
    """ Create Custom Record """

    _name = 'custom.record'
    _description = 'Custom Record'

    name = fields.Char(string='Record Name', required=True)
    status = fields.Selection([('draft', 'Draft'), ('completed', 'Completed')], string='Record Status', default='draft', required=True)

    def update_status(self):
        """ Change any records with 'draft' status to 'completed' """

        records = self.search( [('status','=', 'draft')] )
        for record in records:
            record.status = 'completed'