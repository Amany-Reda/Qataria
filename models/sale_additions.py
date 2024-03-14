from odoo import fields, models, api

PROCUREMENT_PRIORITIES = [('0', 'Normal'), ('1', 'Urgent')]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    driver = fields.Many2one("hr.employee", string="Driver", store=True, readonly=False, tracking=True, required=True)
    current_balance = fields.Float(string="Current Balance", related='partner_id.payment_amount_due', store=False,
                                   readonly=True)

    previous_balance = fields.Float(compute="_compute_total", string="Previous Balance", store=False, readonly=True)

    @api.depends("amount_total")
    def _compute_total(self):
        for record in self:
            record.previous_balance = record.current_balance - record.amount_total

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['driver'] = self.driver.id
        return invoice_vals
