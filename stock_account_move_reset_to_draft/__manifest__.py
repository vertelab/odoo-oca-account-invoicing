# Copyright 2024 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock account move reset to draft",
    'summary': "Resets stock journal entries to draft.",
    'description': '''
Stock account move reset to draft
=================================

    Resets stock journal entries to draft.

    Features:

        - Extends Odoo: Builds on account.move.
    ''',
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/stock_account_move_reset_to_draft",
    "version": "18.0.1.0.0",
    # Real dependency is stock_account but we need purchase_stock in tests
    "depends": ["purchase_stock"],
    "license": "AGPL-3",
    "category": "Warehouse Management",
    "installable": True,
    "maintainers": ["victoralmau"],
}
