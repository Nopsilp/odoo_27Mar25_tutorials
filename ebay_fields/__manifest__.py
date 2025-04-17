{
    'name': 'eBay Fields',
    'version': '18.0.1.0.0',
    'description': 'Add ebay fields to the existing "product.product" view',
    'summary': 'Learn how to add more fields about eBay to the existing "product.product" view. The code is from https://github.com/ffaemy/my_odoo_modules/blob/main/ebay_fields/ebay_fields.zip  This module is for learning only',
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'category': 'Inventory',
    'license': 'LGPL-3', 
    'depends': [
        'base',
        'product',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/view_ebay_fields.xml',

    ],
    'auto_install': False,
    'application': False,
}