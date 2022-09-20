# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """Description""",

    'description': """
        
    """,

    'author': "STeSI",
    'website': "https://www.stesi.eu",


    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application':True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/reparto.xml',
        'views/stanza.xml'

    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
