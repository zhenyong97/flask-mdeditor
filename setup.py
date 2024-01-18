# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='Flask-MDEditor',
    version='0.1.5',
    packages=['flask_mdeditor'],
    license='MIT',
    description='MDEditor integration for Flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/callmehero/flask-mdeditor',
    author='Ziscli',
    author_email='lzyong2019@gmail.com',
    include_package_data=True,
    install_requires=[
        'Flask>=2',
        'wtforms',
        'flask_wtf'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

