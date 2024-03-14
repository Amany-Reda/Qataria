from odoo import api, fields, models

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]


class QatAccount(models.Model):
    _inherit = "account.move"

    driver = fields.Many2one('hr.employee', string="Driver", store=True, readonly=False, tracking=True, required=True)
    current_balance = fields.Float(string="Current Balance", related='partner_id.payment_amount_due', store=False,
                                   readonly=True)

    previous_balance = fields.Float(compute="_compute_total", string="Previous Balance", store=False, readonly=True)

    @api.depends("amount_total")
    def _compute_total(self):
        for record in self:
            record.previous_balance = record.current_balance - record.amount_total
