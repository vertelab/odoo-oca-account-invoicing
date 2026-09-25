# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Update Invoice's Due Date",
    'summary': "Adds a due date field to invoices.",
    'description': '''
Update Invoice's Due Date
=========================

    Adds a due date field to invoices.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on account.move.
    ''',
    "version": "18.0.1.0.1",
    "author": "Vauxoo, Odoo Community Association (OCA)",
    "maintainers": ["luisg123v", "CarlosRoca13"],
    "category": "Accounting",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/account_invoice_date_due",
    "license": "AGPL-3",
    "depends": ["account"],
    "demo": [],
    "data": ["security/security.xml", "views/account_move_date_due.xml"],
    "installable": True,
    "auto_install": False,
}
