#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Little Physics Game',
    'author': 'Aleksandr Yeganov',
    'url': 'https://github.com/nindzadza/Physics-and-AI-Simulation',
    'download_url': 'Where to download it.',
    'author_email': 'absolutnik@gmail.com',
    'version': '0.1',
    'install_requires': ['python-kivy'],
    'packages': ['python-kivy'],
    'scripts': [],
    'name': 'Circles'
}

setup(**config)

