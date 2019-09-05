git subtree add --prefix=custom-addons/oca-website https://github.com/OCA/website.git 12.0 --squash
./odoo-bin -c odoo.conf --dev=all


Required Modules
    'depends': ['base',
                'mail',
                'pp_geography',
                'hr_employee_id',
                'hr_employee_firstname',
                'hr_payroll_cancel',
                'hr_employee_document',
                'hr_employee_service_contract',
                'partner_contact_personal_information_page',
                'l10n_th_partner',
                'date_range'],
