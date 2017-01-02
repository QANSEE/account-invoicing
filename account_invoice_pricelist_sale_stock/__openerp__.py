# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Account Invoice Pricelist Sale - Stock',
    'summary': 'Set pricelist from SO in invoice created from picking.',
    'author': 'Therp BV,Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'website': 'http://therp.nl',
    'category': 'Sales',
    'version': '8.0.1.0.0',
    'depends': [
        'account_invoice_pricelist_sale',
        'stock',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
