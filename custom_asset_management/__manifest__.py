{
    'name': 'Asset Management',
    'version': '18.0.1.0.0',
    'summary': 'A module for managing assets.',
    'description': """
        This module allows you to manage assets.
        - Asset create
        - Asset Validation and Categorization
        *** This is for testing only ***
    """,
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'category': 'Productivity',
    'license': 'LGPL-3', 
    'depends': ['base', 'hr'],
    "data": [
        "security/ir.model.access.csv",
        "views/asset_asset_views.xml",
        "views/asset_category_views.xml",
        "views/actions.xml",
        "views/menus.xml",
    ],

    'installable': True,
    'application': True,

}
