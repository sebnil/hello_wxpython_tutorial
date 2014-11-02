__author__ = 'sebnil'
import pyinstaller_helper

pyinstaller_helper.build({
    'script': 'hello_wxpython.py',
	'icon_win': 'icon/banana.ico',
	'icon_osx': 'icon/banana.icns',
    'application_name': 'hello wxpython',
    'version': '1.0.0.1',
    'company_name': u'Example',
    'product_name': u'Hello wxPython',
    'internal_name': 'product_name',
    'original_filename': u'Hello wxPython',
    'file_description': 'Lorem ipsum.',
    'legal_copyright': 'your@email.com',
    'legal_trademark': ''
})