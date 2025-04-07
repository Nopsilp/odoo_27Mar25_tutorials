from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta


class SCheduledTask(models.Model):
    _name = 'custom.automation.task'
    _description = 'Automated Task Example'
    
    @api.model
    def auto_archive_orders(self):
        """
        This function is for archiving sale orders over 6 months automatically.
        """

        six_months_ago = fields.Datetime.subtract(fields.Datetime.now(), months=6)
        orders = self.env['sale.order'].search([
            ('date_order', '<', six_months_ago),
            ('state', 'in', ['draft', 'sale'])
        ])

        for order in orders:
            order._write({'state': 'cancel'})