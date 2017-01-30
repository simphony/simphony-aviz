import os

from setuptools import setup, find_packages

with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()

VERSION = '0.4.0.dev0'


def write_version_py(filename=None):
    if filename is None:
        filename = os.path.join(
            os.path.dirname(__file__), 'simphony_aviz', 'version.py')
    ver = """\
version = '%s'
"""
    fh = open(filename, 'wb')
    try:
        fh.write(ver % VERSION)
    finally:
        fh.close()


write_version_py()

setup(
    name='simphony_aviz',
    version=VERSION,
    author='SimPhoNy, EU FP7 Project (Nr. 604005) www.simphony-project.eu',
    description='The aviz visualisation plugin for SimPhoNy',
    long_description=README_TEXT,
    entry_points={
        'simphony.visualisation': ['aviz = simphony_aviz']},
    packages=find_packages(),
    install_requires=["simphony>=0.5"]
    )
