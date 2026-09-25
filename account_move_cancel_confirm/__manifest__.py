# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Move Cancel Confirm",
    'summary': "Asks for confirmation before cancelling a journal entry.",
    'description': '''
Account Move Cancel Confirm
===========================

    Asks for confirmation before cancelling a journal entry.

    Features:

        - Focused Fix: A small, targeted improvement to standard Odoo behaviour.
    ''',
    "version": "18.0.1.0.1",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "category": "Usability",
    "license": "AGPL-3",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/account_move_cancel_confirm",
    "depends": ["base_cancel_confirm", "account"],
    "installable": True,
    "maintainers": ["kittiu"],
}
