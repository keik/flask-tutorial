#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os
import sys
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, 'hello_flask'))

setup(
    name='hello_flask',
    version='0.0.1-pre',
    description='Example application for Flask tutorials',
    author='keik',
    author_email='k4t0.kei@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1'
    ],
    tests_require=[
    ],
    classifiers=[
    ],
    data_files=[
    ],
    scripts=['bin/hello_flask'],
    test_suite='hello_flask.tests.suite',
)
