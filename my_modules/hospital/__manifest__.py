# -*- coding: utf-8 -*-
{
    'name': 'Hospital System',
    'version': '1.0.0',
    'summary': 'Module for managing a hospital system including clinics.',
    'description': """
Hospital System Module
======================
This module provides a system to manage clinics, including opening and closing times.
    """,
    'category': 'Healthcare',
    'author': 'Telemachus',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/clinic_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
