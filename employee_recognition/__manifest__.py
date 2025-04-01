{
    'name': 'Employee Recognition',
    'version': '18.0.1.0.0',
    'summary': "App to manage employees' recognition and rewards",
    'description':""" 
        A custom module to manage employee recognition and rewards:
        - Track achievements
        - Assign points
        - Redeem rewards
        - Generate reports
    """,
    'author': 'imheart',
    'website': 'https://example.com',
    'category': 'Human Resources',
    'license': 'LGPL-3', 
    'depends': ['base', 'hr',],
    "data": [
        "security/ir.model.access.csv",
        "views/achievement_type.xml",
        "views/achievement_views.xml",
        "views/actions.xml",
        "views/menus.xml",
        "views/reward_views.xml"
    ],

    'installable': True,
    'application': True,        
}