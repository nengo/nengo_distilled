#!/usr/bin/env python
import imp
import io
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import find_packages, setup  # noqa: F811


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

root = os.path.dirname(os.path.realpath(__file__))
version_module = imp.load_source(
    'version', os.path.join(root, 'nengo_distilled', 'version.py'))
description = "Distilled backend for Nengo."
long_description = read('README.rst', 'CHANGES.rst')

url = "https://github.com/nengo/nengo-distilled"
setup(
    name="nengo-distilled",
    version=version_module.version,
    author="Applied Brain Research",
    author_email="info@appliedbrainresearch.com",
    packages=find_packages(),
    include_package_data=True,
    scripts=[],
    url=url,
    license="%s/blob/master/LICENSE.md" % url,
    description=description,
    long_description=long_description,
    install_requires=[
        "nengo",
    ],
)
