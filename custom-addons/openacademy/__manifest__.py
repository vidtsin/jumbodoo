
{
    'name': "openacademy",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Kitti U.",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'board'],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/wizard_view.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports/report.xml',
    ],
    # Only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
