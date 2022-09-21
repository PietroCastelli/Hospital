
{
    'name': "Hospital",

    'summary': """Application to run an hospital""",

    'description': """
    """,

    'author': "STeSI",
    'website': "https://www.stesi.eu",


    'category': 'Human Resources',
    'version': '14.0.1',


    'depends': ['base'],
    'application':True,


    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/department.xml',
        'views/room.xml'

    ],


}
