"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

package_dir = path.abspath(path.dirname(__file__))
with open(path.join(package_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='notes',
    version='0.1.0',
    description=long_description,
    long_description=long_description,
    url='',
    author='Jason Brazeal',
    author_email='jsonbrazeal@gmail.com',
    license='',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='notes',
    packages=find_packages(exclude=['tests, build, node_modules']),
    install_requires=[
        'click',
        'Flask',
        'Flask-Webpack',
        'itsdangerous',
        'Jinja2',
        'Markdown',
        'MarkupSafe',
        'py-gfm',
        'Pygments',
        'Werkzeug',
    ],
)
