import re
from setuptools import setup


# Requirements
requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Version Info
version = ""
with open("mk8dx/__init__.py") as f:

    search = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if search is not None:
        version = search.group(1)

    else:
        raise RuntimeError("Could not grab version string")

if not version:
    raise RuntimeError("version is not set")

# README
readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name='mk8dx',
    author='sheat',
    url='https://github.com/sheat-git/mk8dx.py',
    version=version,
    packages=['mk8dx', 'mk8dx.lounge_api'],
    license='MIT',
    description='To help to develop something about mk8dx',
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown'
)
