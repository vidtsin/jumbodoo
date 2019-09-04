# -*- coding: utf-8 -*-
{
    'name': "pp_employee",

    'summary': """
       PP Employee module customized for Jumbo Industry co., ltd. 
    """,
    'description': """
       PP Employee module customized for Jumbo Industry co., ltd. This will install the following components:
       -
       -
       -
       -
    """,

    'author': "Jakkrit S.",
    'website': "https://ppsmartbot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Employee',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'pp_geography'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}