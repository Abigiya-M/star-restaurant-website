from odoo import models, fields, api

class MenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Menu Item'

    name = fields.Char(required=True)
    description = fields.Text()
    price = fields.Float(required=True)
    category_id = fields.Many2one('restaurant.menu.category')
    image = fields.Image()

    # Link to product.template
    product_id = fields.Many2one('product.template', string="Linked Product", readonly=True)

    @api.model
    def create(self, vals):
        # Create MenuItem first
        record = super().create(vals)

        # Create corresponding product.template
        product = self.env['product.template'].create({
            'name': record.name,
            'list_price': record.price,
            'type': 'consu',
            'available_in_pos': True,
            'image_1920': record.image,
        })

        # Link product to MenuItem
        record.write({'product_id': product.id})

        return record

    def write(self, vals):
        res = super().write(vals)
        for record in self:
            if record.product_id:
                record.product_id.write({
                    'name': record.name,
                    'list_price': record.price,
                    'image_1920': record.image,
                })
        return res

    def unlink(self):
        # Delete linked product.template if MenuItem is deleted
        for record in self:
            if record.product_id:
                record.product_id.unlink()
        return super().unlink()
