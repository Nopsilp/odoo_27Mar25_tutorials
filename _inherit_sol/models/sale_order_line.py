from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount_custom = fields.Float(string = "Custom Discount (%)")