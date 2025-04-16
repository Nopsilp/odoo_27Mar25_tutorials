{
    'name': 'Custom KPI Dashboard',
    'version': '18.0.1.0.0',
    'description': """
        This module is for learning how to build KPI dashboard.
        From: https://github.com/ffaemy/my_odoo_modules/blob/750e6faf679ae431a0078382098cc5114b149b20/dashboard_kpi/dashboard_kpi/models/dashboard.py
    """,
    'summary': 'Custom KPI Dashboard',
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'category': 'Reporting',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale',
        'stock',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_view.xml',
    ],
    'auto_install': False,
    'application': True,
    'assets': {
        "web.assets_backend": [
            'custom_kpi_dashboard/static/src/dashboard.css'
        ],
    }
}