# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='eureka-inventory',
    description='eureka ansible inventory',
    author='Pablo Diaz',
    author_email='padilo@gmail.com',
    version='0.1',
    install_requires=['simplejson', 'unirest', 'click'],
    packages=['app'],
    entry_points={
        'console_scripts': [
            'eureka-inventory = app.cli:run_cli',
            'eureka-inventory-get = app.getme:get_me'
        ]
    }

)

