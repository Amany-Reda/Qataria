{
    'name': 'Some Changes In Qataria Company',
    'version': '16.0.0.0',
    'summary': 'Accounting and Sales modification for Qataria Project',
    'description': """This module helps to modify some things in sales and Accounting modules""",
    'website': 'https://www.gate-its.com',
    'author': "Gate ITS",
    'category': 'Accounting/Customer/Invoices & Sales/Quotation',
    'depends': [
        'sale',
        'account',
        'hr',

    ],
    'data': [
        'views/qat_account_move_views.xml',
        'views/qat_sale_order_views.xml',
        'report/qat_report.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
    'auto_install': False,
}
