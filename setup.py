#!/usr/bin/python3

import setuptools

install_requires = []

setuptools.setup(
    name="some_utils",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'notify = notifier:main',
        ],
    },
    include_package_data=True,
    )