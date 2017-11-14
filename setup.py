# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-bootcamp',
    version='0.1.0',
    description='Package for InfoScout Python Bootcamp',
    long_description=readme,
    author='Dana Ford',
    author_email='dana@infoscoutinc.com',
    url='https://github.com/infoscout/python-bootcamp',
    license=license,
    packages=find_packages()
)
