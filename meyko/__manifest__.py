# Copyright 2021 Vauxoo
# License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Instance Creator',
    'summary': '''
    Instance creator for meyko. This is the app.
    ''',
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'LGPL-3',
    'category': 'Installer',
    'version': '14.0.1.0.0',
    'depends': [
        'account_accountant',
        'account_consolidation',
        'sale_crm',
        'sale_renting',
        'approvals',
        'documents',
        'project',
        'industry_fsm',
        'helpdesk',
        'hr_timesheet',
        'hr_expense',
        'hr_recruitment',
        'mrp',
        'maintenance',
        'purchase_stock',
        'point_of_sale',
        'website_sale',
        'website_slides',
    ],
    'test': [
    ],
    'data': [
        'data/res_company_data.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
