"""
Odoo Asset Management Module

This module defines the asset model and handles asset depreciation,
assignment to employees, and validation of asset categories.
"""

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class AssetAsset(models.Model):

    """
    Represents an asset, including its name, category, value, purchase date, 
    depreciation rate, assigned employee, and current value.
    """

    _name = 'asset.asset'
    _description = 'Asset'

    name = fields.Char(string="Asset", required=True)

    #  Refer to asset.category model in AssetCategory in asset_category.py
    #  The default is the 1st asset category found
    category_id = fields.Many2one(
        'asset.category',
        string='Category',
        required=True,
        default=lambda self: self.env['asset.category'].search([], limit=1),  
    )

    value = fields.Float(string='Purchase Value', required=True, digits=(16, 2))
    purchase_date= fields.Date(
        string='Purchase Date',
        default=fields.Date.context_today,
        required=True,
    )
    depreciation_rate= fields.Float(string='Depreciation Rate(%)', required=True, digits=(16, 2))

    #  compute the current value of the asset
    current_value = fields.Float(
        string='Current Value',
        compute='_compute_current_value',
        store=True,
    )

    #  Refer to hr.employee in HR module
    #  The default is the 1st employeed found
    employee_id = fields.Many2one(
        string='Assigned To',
        comodel_name='hr.employee',
        default=lambda self: self.env['hr.employee'].search([], limit=1),
    )

    
    @api.depends('value', 'depreciation_rate', 'purchase_date')
    def _compute_current_value(self):
        """
        Computes the current value of the asset based on purchase value,
        depreciation rate, and purchase date.
        """

        for record in self:
            if record.purchase_date:
                years = (fields.Date.today() - record.purchase_date).days / 365.0
                record.current_value = record.value *(1 - (record.depreciation_rate / 100) * years)
    

    @api.constrains('category_id', 'employee_id')
    def _check_m2o_fields(self):
        """
        Ensures that the asset has a valid category and is assigned to an employee.
        Raises ValidationError if either field is missing.
        """

        for record in self:
            if not record.category_id:
                raise ValidationError('Asset must belong to a category.')
            if not record.employee_id:
                raise ValidationError('Asset must be assigned to an employee.')
