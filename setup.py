#!/usr/bin/env python
from os import path
from setuptools import setup

def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='jsentry',
    description="Javascript error tracking for Django Sentry.",
    version='1.0',
    maintainer="Stephen Diehl",
    maintainer_email="stephen.m.diehl@gmail.com",
    install_requires=(
        'django',
        'django-sentry',
    ),
    packages=[
        'jsentry',
    ],
    package_data={
        'jsentry' : ['static/*'],
    },
)
