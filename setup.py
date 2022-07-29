from setuptools import setup


# Requirements
requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# README
readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name='mk8dx',
    author='sheat',
    url='https://github.com/sheat-git/mk8dx.py',
    version='1.0.6',
    packages=['mk8dx', 'mk8dx.lounge_api'],
    license='MIT',
    description='To help to develop something about mk8dx',
    install_requires=requirements,
    long_description=readme,
    long_description_content_type='text/markdown'
)
