#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['djangorestframework-gis', 'shapely']

setup(
    author="Wholesail Networks",
    author_email='nick.bogle@ziply.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Netbox GeoDjango Plugin for visualizing sites, cables, circuits, etc.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='netbox_geo',
    name='netbox_geo',
    packages=find_packages(include=['netbox_geo', 'netbox_geo.*']),
    test_suite='tests',
    url='https://github.com/wholesailnetworks/netbox_geo',
    version='0.1.0',
    zip_safe=False,
)
