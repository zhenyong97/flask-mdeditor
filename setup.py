# -*- coding:utf-8 -*-
import os
from setuptools import find_packages, setup
from codecs import open

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Flask-MDEditor',
    version='0.1',
    packages=['flask_mdeditor'],
    include_package_data=True,
    license='MTI License',
    description='A simple FLASK app to edit markdown text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/callmehero/flask-mdeditor',
    author='ZiscLi',
    author_email='lzyong2019@gmail.com',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

