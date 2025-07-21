from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class RestaurantWebsite(http.Controller):

    @http.route(['/','/homepage'], type='http', auth='public', website=True)
    def homepage(self, **kwargs):
        return request.render('star_Restaurant.homepage')

    @http.route('/menu', type='http', auth='public', website=True)
    def menu(self, **kwargs):
        categories = request.env['restaurant.menu.category'].sudo().search([])
        return request.render('star_Restaurant.menu_page', {
            'categories': categories
        })

    @http.route('/reservation_page', type='http', auth='public', website=True)
    def reserve(self, **kwargs):
        # Fetch all tables from your restaurant.table model
        tables = request.env['restaurant.table'].sudo().search([])
        return request.render('star_Restaurant.reservation_page', {
            'tables': tables
        })

    @http.route('/reservation/submit', type='http', auth='public', website=True, methods=['POST'])
    def reservation_submit(self, **post):
        time_str = post.get('time')  # e.g. '14:30'
        number_of_people = post.get('number_of_people')
        table_id = post.get('table_id')

        # Convert '14:30' → 14.5
        if time_str:
            hours, minutes = map(int, time_str.split(':'))
            time_value = hours + minutes / 60.0
        else:
            time_value = 0.0

        # Create reservation record
        request.env['restaurant.reservation'].sudo().create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'date': post.get('date'),
            'time': time_value,
            'number_of_people': int(number_of_people) if number_of_people else 1,
            'note': post.get('note'),
            'table_id': int(table_id) if table_id else False,
        })

        return request.redirect('/reservation_thank_you')

    @http.route('/reservation_thank_you', type='http', auth='public', website=True)
    def reservation_thank_you(self, **kwargs):
        return request.render('star_Restaurant.reservation_thank_you')

    # === Contact Us Page ===

    @http.route('/contact_us', type='http', auth='public', website=True)
    def contact_us(self, **kwargs):
        return request.render('star_Restaurant.contact_us')

    @http.route('/contact_us/submit', type='http', auth='public', website=True, methods=['POST'])
    def contact_us_submit(self, **post):
        # Log submitted data (replace with your own logic: save to model or send email)
        _logger.info(f"Contact form submitted: {post}")

        # For now, just redirect to a thank you page
        return request.redirect('/contact_us_thank_you')

    @http.route('/contact_us_thank_you', type='http', auth='public', website=True)
    def contact_us_thank_you(self, **kwargs):
        return request.render('star_Restaurant.contact_us_thank_you')
