import os
from setuptools import 
find_packages, setup

with

open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README  = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup = (
    name = 'The TechBlog',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    license = 'No License',

    description = 'The TechBlog is a simple blog application created using the django framework where, the admin and registered users and groups can post stories and blogs according to their liking.'

    long_description = README,

    url = 'http://127.0.0.1:8000'
    author = 'Diwash', 'Bibek', 'Vivek', 'Karan',
    author_email = 'diwashchhetri070296@gmail.com',

    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django Framework',
        'Operating System :: OS Independent',
        'Programming Language :: Python PL',
        'Topic :: Internet :: WWW/HTTP',
        'Project Intended For :: Ardent CompuTech',

    ]
)