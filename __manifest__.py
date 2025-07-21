{
    'name': 'star_Restaurant',
    'version': '1.0',
    'summary': 'A restaurant website with menu and reservations',
    'author': 'Abby M',
    'depends': ['website'],
    'data': [
        'views/backend_views.xml',
        'security/ir.model.access.csv',
        'views/homepage.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/backend_menu.xml',
        # 'views/gallary.xml',
        'views/menu.xml',
        'views/contact_us.xml',
        'views/reservation.xml',
        'views/reservation_thankyou.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'star_Restaurant/static/src/css/star_restaurant_header.css',
        ],
    },
    'installable': True,
    'application': True,
}
