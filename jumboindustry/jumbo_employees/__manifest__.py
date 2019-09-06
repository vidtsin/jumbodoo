# -*- coding: utf-8 -*-
{
    'name': "Jumbo Employees Management",

    'summary': """
        Jumbo Employees Management module developed for Jumbo Industry
    """,

    'description': """
        Jumbo Employees Management module developed for Jumbo Industry
    """,

    'author': "Jakkrit S.",
    'website': "https://www.ppsmartproduct.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Employee',
    'version': '12.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}