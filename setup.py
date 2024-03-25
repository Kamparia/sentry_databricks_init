#!/usr/bin/env python3
import os 
import sys

from setuptools import setup, find_packages

version = "0.0.1"

long_description = open('README.md').read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name="sentry_databricks_init",
    version=version,
    author="Olaoye Anthony Somide",
    author_email="somideolaoye@gmail.com",
    license="MIT",
    url="https://github.com/Kamparia/sentry_databricks_init",
    description="An example package to initialize Sentry SDK in Databricks notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='sentry databricks init sdk',
    packages=find_packages(),
    python_requires=">=3.8",    
    install_requires=[
        "sentry-sdk>=1.43.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
