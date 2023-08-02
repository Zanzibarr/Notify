#!/usr/bin/python3

import setuptools

setuptools.setup(
    name="notifier",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'notify = notify_app:main',
        ],
    },
    include_package_data=True,
    )