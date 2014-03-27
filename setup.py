#!/usr/bin/env python

from distutils.core import setup

setup(name='tenvislib',
      version='1.0',
      description='Low-Cost Network Camera (TENVIS) library',
      author='Yuki SUGA',
      author_email='ysuga@sugarsweetrobotics.com', 
      url='http://www.sugarswwetrobotics.com', 
      packages=['tenvis'],
      package_dir={'tenvis': 'tenvis'}
     )
