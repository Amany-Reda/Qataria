from odoo import fields, models

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    discount_amount = fields.Float(string="Discount(AMT)", digits="Discount")
