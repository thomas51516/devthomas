{
    'name': 'School management',
    'version': '1.0',
    'description': 'This module allows you to manage a school',
    'summary': 'This module allows you to manage a school',
    'author': 'Thomas',
    'website': 'https://erptogo.net',
    'license': 'LGPL-3',
    'category': 'School',
    'depends': [
        'base','mail','web','sale_management'
    ],
    'data': [
        'views/student_view.xml',
        'views/student_class_view.xml',
        'views/school_course_view.xml',
        'views/sale_order_view.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': False,
    'application': False,
    'sequence':0,
}