"""Setup script for zinnia-theme-bootstrap"""
from setuptools import setup
from setuptools import find_packages

import zinnia_bootstrap

setup(
    name='zinnia-theme-bootstrap3',
    version=zinnia_bootstrap3.__version__,

    description='Bootstrap 3.0 theme for django-blog-zinnia',
    long_description=open('README.rst').read(),

    keywords='django, blog, weblog, zinnia, theme, skin, bootstrap',

    author=zinnia_bootstrap3.__author__,
    author_email=zinnia_bootstrap3.__email__,

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=zinnia_bootstrap3.__license__,
    include_package_data=True,
    zip_safe=False
)