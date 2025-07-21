from odoo import models, fields

class RestaurantTable(models.Model):
    _name = 'restaurant.table'
    _description = 'Restaurant Table'

    name = fields.Char(required=True)  # e.g., "Table 1"
    capacity = fields.Integer(default=4)
