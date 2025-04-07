{
    'name': 'Cron Management',
    'version': '18.0.1.0.0',
    'description': 'To implement cron tasks',
    'summary': 
        """
        This module provides functionality to create and manage scheduled actions (cron jobs) 
        - archiving old records
        - sending scheduled emails
        - system maintenance.
        """,
    'author': 'Nop_BKK',
    'website': 'https://example.com',
    'license': 'LGPL-3',
    'category': 'Automation',
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'data/scheduled_action.xml',
    ],
    'auto_install': False,
    'application': False,
    'assets': {        
    }
}