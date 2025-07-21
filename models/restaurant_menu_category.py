from odoo import models, fields

class MenuCategory(models.Model):
    _name = 'restaurant.menu.category'
    _description = 'Menu Category'

    name = fields.Char(required=True)
    menu_item_ids = fields.One2many(
        'restaurant.menu.item',
        'category_id',
        string='Menu Items'
    )
