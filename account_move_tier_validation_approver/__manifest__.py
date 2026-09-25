# Copyright 2021 ForgeFlow, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Move Tier Validation Approver",
    'summary': "Adds tier validation approvers to journal entries.",
    'description': '''
Account Move Tier Validation Approver
=====================================

    Adds tier validation approvers to journal entries.

    Features:

        - UI Integration: Extends 3 view(s) in the Odoo interface.
        - Extends Odoo: Builds on account.move, tier.definition.
    ''',
    "version": "18.0.1.0.0",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": ["account_move_tier_validation"],
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/account_move_tier_validation_approver",
    "data": [
        "views/account_move_views.xml",
        "views/res_partner_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
