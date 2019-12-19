#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-error-for-skips',
    version='2.0.0',
    author='Jan Katins',
    author_email='jasc@gmx.net',
    maintainer='Jan Katins',
    maintainer_email='jasc@gmx.net',
    license='MIT',
    url='https://github.com/jankatins/pytest-error-for-skips',
    description='Pytest plugin to treat skipped tests a test failure',
    long_description=read('README.md'),
    py_modules=['pytest_error_for_skips'],
    install_requires=['pytest>=5'],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'error-for-skips = pytest_error_for_skips',
        ],
    },
)
