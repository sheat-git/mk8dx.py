from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='mk8dx',
    packages=['mk8dx'],
    version='1.0.1',
    install_requires=_requires_from_file('requirements.txt')
)
