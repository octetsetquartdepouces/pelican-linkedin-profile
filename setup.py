# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = __import__('pelican-linkedin-profile').__version__
download_url = 'https://github.com/octetsetquartdepouces/pelican-linkedin-profile/archive/{}.zip'.format(version)

setup(name='pelican-linkedin-profile',
      version=version,
      url='https://github.com/octetsetquartdepouces/pelican-linkedin-profile',
      download_url=download_url,
      author="Kyah",
      author_email="contact@octetsetquartdepouces.net",
      maintainer="Kyah",
      maintainer_email="contact@octetsetquartdepouces.net",
      description="Extract your linkedin profile and allow you to use those informations in Pelican's pages",
      long_description=open("README.rst").read(),
      license='GPLv2',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      install_requires=['pelican', 'python-linkedin'],
      package_data={'': ['LICENSE', ]},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing',
      ],
      zip_safe=True,
      )
