# -*- coding: utf-8 -*-
{
    'name': "CRM Dashboard",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'category': 'CRM Dashboard',
    'sequence': 2,
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'crm', 'sale_management'],
    'data':
        [
            "views/crm_team_views.xml",
            "views/dashboard_menu_views.xml",
        ],
    'assets': {
        'web.assets_backend': [
            'crm_dashboard/static/src/js/dashboard.js',
            'crm_dashboard/static/src/xml/dashboard.xml',
        ],
    },

}
