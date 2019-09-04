# -*- coding: utf-8 -*-
{
    'name': "PPSmart Geolocation",

    'summary': "Thailand province and city names",

    'description': """PPSmart Geography module provides provinces and cities info.
    Icons made by https://www.flaticon.com/authors/freepik from https://www.flaticon.com/ is licensed by Creative Commons BY 3.0
    """,

    'author': "Jakkrit S.",
    'website': "https://ppsmartbot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Thai_Geolocation',
    'version': '12.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/province_data.xml',
        'data/amphur_data.xml',
        'data/district_data.xml',
        'data/zipcode_data.xml',
        'views/geolocation_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
