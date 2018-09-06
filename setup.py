# !/uer/bin/env python3
# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('base/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='AppTester',
    version=version,
    url='https://github.com/medivhXu/Apper',
    license='BSD',
    author='MedivhXu',
    author_email='medivh_xu@outlook.com',
    description='本程序参照pyse的思路改编而成',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['selenium>=3.12.0', 'parameterized>=0.6.1', 'Appium-Python-Client', 'pymysql'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Ubuntu',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries ::Testing'
    ]
)
