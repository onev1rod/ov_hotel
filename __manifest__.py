{
    'name': 'Hotel management - OV',
    'description': 'Manage rooms booking',
    'summary': 'Hotel Management, Hotel, Room Booking Odoo, Amenities, Rooms, Booking',
    'author': 'onev1rod',
    'version': '17.0.1.0.1',
    'category': 'Industries',
    'sequence': '1',
    'depends': ['base', 'mail', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_data_sequence.xml',
        'data/hotel_amenity_data.xml',
        'data/hotel_room_data.xml',
        'wizard/cancel_room_booking_views.xml',
        'report/room_booking_report_template.xml',
        'views/room_booking_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_amenity_views.xml',
        'views/hotel_service_views.xml',
        'views/product_template_views.xml',
        'views/search_available_room_views.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'images': [],
    'application': 'True',
    'installable': 'True',
    'license': 'LGPL-3',
    'assets': {},
}
