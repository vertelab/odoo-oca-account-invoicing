# Copyright (C) 2019-Today: Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Stock Picking Invoicing",
    'summary': "Adds invoicing to stock transfers.",
    'description': '''
Stock Picking Invoicing
=======================

    Adds invoicing to stock transfers.

    Features:

        - Guided Wizards: Step-by-step dialogs for data entry.
        - UI Integration: Extends 3 view(s) in the Odoo interface.
        - Extends Odoo: Builds on account.move, stock.invoice.state.mixin, stock.move, stock.picking.
    ''',
    "version": "18.0.1.0.0",
    "category": "Warehouse Management",
    "author": "Agile Business Group,Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/stock_picking_invoicing",
    "license": "AGPL-3",
    "depends": [
        "stock",
        "account",
        "stock_picking_invoice_link",
        "base_view_inheritance_extension",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/stock_invoice_onshipping_view.xml",
        "wizards/stock_return_picking_view.xml",
        "views/stock_move_views.xml",
        "views/stock_picking_views.xml",
        "views/stock_picking_type_views.xml",
    ],
    "demo": ["demo/stock_picking_demo.xml"],
    "installable": True,
}
