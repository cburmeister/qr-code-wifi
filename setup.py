from setuptools import setup

setup(
    name='qr_code_wif',
    version='0.1',
    py_modules=['qr_code_wifi'],
    install_requires=[
        'Click==6.7',
        'pypng==0.0.18',
        'pyqrcode==1.2.1',
    ],
    entry_points='''
        [console_scripts]
        qr_code_wifi=qr_code_wifi:create
    ''',
)
