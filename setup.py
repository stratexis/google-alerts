#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='google-alerts',
    version='0.0.1',
    description='Abstraction to manage Google Alerts and output',
    url="https://github.com/9b/google-alerts",
    author="Brandon Dixon",
    author_email="brandon@9bplus.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[''],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ],
    package_data={
        'pyhottop': [],
    },
    entry_points={
        'console_scripts': [
            'pyhottop-test = pyhottop.cli.config:main'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    keywords=['google', 'alerts', 'automation', 'administration'],
    download_url='https://github.com/9b/google-alerts/archive/master.zip'
)