#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re

from os import path
from codecs import open
from setuptools import setup, Extension, find_packages

here = path.abspath(path.dirname(__file__))
HOME = os.environ['HOME']

version_file_contents = open(
    path.join(here, 'pysupwsdpocket/_version.py'), encoding='utf-8').read()
VERSION = re.compile(
    '__version__ = \"(.*)\"').search(version_file_contents).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# This call to setup() does all the work
setup(
    name="pysupwsdpocket",
    version=VERSION,
    description="Just a Python Version of SupWSD Pocket: A software suite for SUPervised Word Sense Disambiguation",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rodriguesfas/PySupWSDPocket",
    author="RodriguesFAS",
    author_email="franciscosouzaacer@gmail.com",

    # What does your project relate to?
    keywords='natural-language-processing nlp natural-language-understanding supwsd wsd',

    # Choose your license
    license="MIT",

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(
        exclude=("tests")
    ),

    include_package_data=True,

    package_data = {'pysupwsdpocket': ['supwsd-pocket.jar']},

    # Create dir.
    data_files=[
        (HOME+'/pysupwsdpocket_models', []),
    ],

    install_requires=[],

    # List required Python versions.
    python_requires='>=3.7',

    entry_points={
        "console_scripts": [
            "pysupwsdpocket=pysupwsdpocket.__main__:main"
        ]
    }

)
