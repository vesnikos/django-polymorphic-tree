#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys

# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv or 'develop' in sys.argv:
    os.chdir('polymorphic_tree')
    try:
        from django.core import management
        management.call_command('compilemessages', stdout=sys.stderr, verbosity=1)
    except ImportError:
        if 'sdist' in sys.argv:
            raise
    finally:
        os.chdir('..')


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-polymorphic-tree',
    version=find_version('polymorphic_tree', '__init__.py'),
    license='Apache 2.0',

    python_requires='>=3',
    install_requires=[
        'django-polymorphic>=3.0',  # Latest to support Django 1.8 and 1.10
        'django-mptt>=0.11.0',
        'django-tag-parser>=3.2',
        'future>=0.12.2',
    ],
    requires=[
        'Django (>=3.1)',
    ],
    extras_require={
      'dev': [
          'tox~=3.20',
      ]
    },
    description="A polymorphic mptt structure to display content in a tree.",
    long_description=read('README.rst'),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/django-polymorphic/django-polymorphic-tree',
    download_url='https://github.com/django-polymorphic/django-polymorphic-tree/zipball/master',

    packages=find_packages(),
    include_package_data=True,


    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 3.1',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
