# Copyright 2017 Creu Blanca
# Copyright 2022 Moduon
# License AGPL-3.0 or later (https://www.gnuorg/licenses/agpl.html).

{
    "name": "Purchase Self Invoice",
    'summary': "Lets suppliers create self-billed invoices.",
    'description': '''
Purchase Self Invoice
=====================

    Lets suppliers create self-billed invoices.

    Features:

        - UI Integration: Extends 4 view(s) in the Odoo interface.
        - Extends Odoo: Builds on account.move.
    ''',
    "version": "18.0.1.0.0",
    "author": "CreuBlanca, Moduon, Odoo Community Association (OCA)",
    "category": "Accounting & Finance",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/account_invoice_supplier_self_invoice",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "data/mail_template_data.xml",
        "views/res_config_settings_views.xml",
        "views/res_partner_views.xml",
        "views/account_move_views.xml",
        "views/report_self_invoice.xml",
    ],
    "installable": True,
}
