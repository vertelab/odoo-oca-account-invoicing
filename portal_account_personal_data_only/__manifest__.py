# Copyright 2018-19 Tecnativa S.L. - David Vidal
# Copyright 2022 Moduon Team SL
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Portal Accounting Personal Data Only",
    'summary': "Lets portal users see only their own accounting data.",
    'description': '''
Portal Accounting Personal Data Only
====================================

    Lets portal users see only their own accounting data.

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    "version": "18.0.1.0.0",
    "category": "Accounting/Accounting",
    "author": "Moduon, Tecnativa, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/portal_account_personal_data_only",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": ["security/security.xml"],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
