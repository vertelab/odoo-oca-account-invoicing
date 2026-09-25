# Copyright 2023 Tecnativa - Pedro M. Baeza
# Copyright 2024 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sales order invoicing by percentage of the quantity",
    'summary': "Invoices a percentage of the ordered quantity.",
    'description': '''
Sales order invoicing by percentage of the quantity
===================================================

    Invoices a percentage of the ordered quantity.

    Features:

        - Guided Wizards: Step-by-step dialogs for data entry.
        - Extends Odoo: Builds on sale.order.line.
    ''',
    "version": "18.0.1.0.0",
    "category": "Sales Management",
    "license": "AGPL-3",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/sale_order_invoicing_qty_percentage",
    "depends": ["sale"],
    "data": ["wizards/sale_advance_payment_inv_views.xml"],
    "installable": True,
    "maintainers": ["pedrobaeza"],
}
