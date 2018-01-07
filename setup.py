from setuptools import setup
from codecs import open
from os import path
from sys import version_info
import re

if version_info < (3, 5):
    raise RuntimeError("aiohttp_sendgrid doesn't suppport Python < 3.5")

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'aiohttp_sendgrid', '__init__.py')) as f:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", f.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine package version.')

setup(name='aiohttp_sendgrid',
      version=version,
      description='SendGrid mail send API wrapper',
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: AsyncIO'
      ],
      keywords='aiohttp sendgrid',
      url='https://github.com/kurlov/aiohttp-sendgrid',
      author='Aleksandr Kurlov',
      author_email='sasha.kurlov@yandex.com',
      license='MIT',
      packages=['aiohttp_sendgrid'],
      zip_safe=False,
      include_package_data=True,
      platforms='any',
      install_requires=['aiohttp>=2.3.7'])
