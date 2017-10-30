# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


def _get_version():
    v_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'pygen', '__init__.py')
    ver_info_str = re.compile(r".*version_info = \((.*?)\)", re.S). \
        match(open(v_file_path).read()).group(1)
    return re.sub(r'(\'|"|\s+)', '', ver_info_str).replace(',', '.')


entry_points = {
    "console_scripts": ["pygen=pygen.cli:pygen"]
}

install_requires = []
tests_requires = []

with open('requirements.txt') as f:
    for r in f:
        install_requires.append(r)

with open('dev_requirements.txt') as f:
    for r in f:
        tests_requires.append(r)

setup(
    name='pygen',
    version=_get_version(),
    long_description=open('README.md').read(),
    author="shenjialong",
    author_email="shenjialong@meituan.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    url="",
    entry_points=entry_points,
    tests_require=tests_requires,
    install_requires=install_requires,
)
