"""Module for managing asset categories"""


from odoo import models
from odoo import fields


class AssetCategory(models.Model):
    """Class for managing asset categories"""
    _name = 'asset.category'
    _description = 'Asset Category'

    name = fields.Char(string="Category Name", required=True)
    description= fields.Text()

