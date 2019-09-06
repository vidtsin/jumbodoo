# -*- coding: utf-8 -*-
{
    'name': "Jumbo Industry Employee Management",

    'summary': """
        Jumbo Co., Ltd. Employee Management""",

    'description': """
        Jumbo Industry Co., Ltd. Employee Management Module developed by
        PPSmartProduct Company.
    """,

    'author': "Jakkrit S.",
    'website': "http://ppsmartproduct.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Employee',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr.employee'],

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