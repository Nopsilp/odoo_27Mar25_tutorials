{
    'name': 'Discounted Products',
    'version': '18.0.1.0.0',
    'description': """
        This module allows users to set discounts on products and provides a custom route to display only discounted products on the shop page.
        Features:
        - Add a discount field to products
        - Filter products with discounts on the shop page
        
        This is from https://github.com/ffaemy/my_odoo_modules/tree/750e6faf679ae431a0078382098cc5114b149b20/shop_discount/discount_products/discount_products

    """,
    'summary': 'Learn how to use Template and Controllers by adding discounts to products and filter discounted products on the shop page.',
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'category': 'Productivity',
    'license': 'LGPL-3', 
    'depends': [
        'website_sale',
    ],
    'data': [
        'views/product_views.xml',
        'views/website_menu_views.xml',
        'views/website_sale_inherit_template.xml'
    ],

    'auto_install': False,
    'application': False,
}