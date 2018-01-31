#!/usr/bin/env python

from setuptools import setup
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

def read_readme():
    with open(os.path.join(here, 'README.md')) as f:
        return f.read()

def get_requirements():
    with open(os.path.join(here, 'requirements.txt')) as f:
        return f.readlines()

setup(
    name = "concourse-blank-resource",
    version = '0.1.0',
    description = 'Concourse CI resource for confirming Concourse behaviour.',
    long_description = read_readme(),
    url = 'https://github.com/petegoo/concourse-blank-resource',
    author = 'PeteGoo',
    classifiers = [
    ],
    keywords = [
    ],
    packages = [ 'blank_resource' ],
    #install_requires = get_requirements(),
    include_package_data = True,
    entry_points = {
        'console_scripts': [
            'check = blank_resource.check:main',
            'in = blank_resource.in_:main',
            'out = blank_resource.out:main',
        ]
    }
)