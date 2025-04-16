{
    'name': 'eBay Fields',
    'version': '18.0.1.0.0',
    'description': 'Add ebay fields to the existing "product.product" view',
    'summary': 'Learn how to add more fields about eBay to the existing "product.product" view',
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