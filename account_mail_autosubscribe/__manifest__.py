# Copyright 2021 Camptocamp (http://www.camptocamp.com).
# @author Iván Todorovich <ivan.todorovich@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Mail Autosubscribe",
    "summary": "Automatically subscribe partners to their company's invoices",
    "version": "18.0.1.0.0",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["ivantodorovich"],
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": ["mail_autosubscribe", "account"],
    "website": "https://vertel.se/apps/odoo-oca-account-invoicing/account_mail_autosubscribe",
    "data": ["data/mail_autosubscribe.xml"],
    "auto_install": True,
}
