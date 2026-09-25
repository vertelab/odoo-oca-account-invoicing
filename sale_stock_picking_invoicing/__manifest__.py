# Copyright (C) 2013-Today - Akretion (<http://www.akretion.com>).
# @author Renato Lima <renato.lima@akretion.com.br>
# @author Raphael Valyi <raphael.valyi@akretion.com>
# @author Magno Costa <magno.costa@akretion.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sales Stock Picking Invocing",
    'summary': "Invoices from stock transfers.",
    'description': '''
Sales Stock Picking Invocing
============================

    Invoices from stock transfers.

    Features:

        - Guided Wizards: Step-by-step dialogs for data entry.
        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on sale.order, sale.order.line, stock.move, stock.picking.
    ''',
    "category": "Warehouse Management",
    "license": "AGPL-3",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/sale_stock_picking_invoicing",
    "version": "18.0.1.0.0",
    "maintainers": ["mbcosta", "renatonlima"],
    "depends": [
        "sale_management",
        "sale_stock",
        "stock_picking_invoicing",
        "stock_picking_invoice_link",
    ],
    "data": [
        "views/res_company_view.xml",
        "views/res_config_settings_view.xml",
        # Wizards
        "wizards/stock_invoice_onshipping_view.xml",
    ],
    "demo": [
        "demo/sale_order_demo.xml",
    ],
    "installable": True,
    "auto_install": False,
}
