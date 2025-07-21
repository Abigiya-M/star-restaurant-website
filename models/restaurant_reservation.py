from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Reservation(models.Model):
    _name = 'restaurant.reservation'
    _description = 'Reservation'

    name = fields.Char('Customer Name', required=True)
    email = fields.Char()
    phone = fields.Char()
    date = fields.Date(required=True)
    time = fields.Float(string="Time (24)", required=True)
    number_of_people = fields.Integer()
    note = fields.Text()
    table_id = fields.Many2one('restaurant.table', string="Table", required=True)

    @api.constrains('date', 'time', 'table_id')
    def _check_table_availability(self):
        for record in self:
            conflicting = self.env['restaurant.reservation'].search([
                ('id', '!=', record.id),
                ('table_id', '=', record.table_id.id),
                ('date', '=', record.date),
                ('time', '=', record.time),
            ])
            if conflicting:
                raise ValidationError(
                    f"The table {record.table_id.name} is already reserved on {record.date} at {record.time}:00."
                )
