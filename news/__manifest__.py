# -*- coding: utf-8 -*-

{
    'name': 'TMC Novedades',
    'summary': 'Odoo module for TMC internal web portal news',
    'version': '10.0.1.0.0',
    'website': 'https://www.tmcrosario.gob.ar',
    'author': 'Tribunal Municipal de Cuentas - Municipalidad de Rosario',
    'license': 'AGPL-3',
    'depends': [u'tmc'],
    'data': [
        u'security/groups.xml',
        u'security/ir.model.access.csv',
        u'views/news.xml',
        u'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
