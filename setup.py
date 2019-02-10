#!/usr/bin/env python3
import setuptools

REQUIREMENTS = open('requirements.txt').read().splitlines()


setuptools.setup(
    name='ged',
    version='1.0',
    description='Parses GEDCOM files and outputs tabular representation.',
    installl_requires=REQUIREMENTS,
    packages=setuptools.find_packages(),
    url='https://github.com/lazorgator/ssw555-gedcom',
)
