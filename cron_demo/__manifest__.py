{
    'name': 'Cron Demo',
    'version': '18.0.1.0.0',
    'description': '',
    'summary': '',
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'license': 'LGPL-3',
    'category': 'Custom',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/actions.xml',
        'views/cron_demo_views.xml',
        'views/menus.xml',        
    ],
    'auto_install': False,
    'application': True,
}