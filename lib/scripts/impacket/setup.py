#!/usr/bin/python
# $Id: setup.py 256 2011-06-08 02:37:58Z gmoreira $

import glob
import os

from distutils.core import setup

PACKAGE_NAME = "Impacket"

setup(name = PACKAGE_NAME,
      version = "0.9.7.0",
      description = "Network protocols Constructors and Dissectors",
      url = "http://oss.coresecurity.com/projects/impacket.html",
      author = "CORE Security Technologies",
      author_email = "oss@coresecurity.com",
      maintainer = "Gustavo Moreira",
      maintainer_email = "gmoreira@gmail.com",
      packages = ['impacket', 'impacket.dcerpc'],
      scripts = glob.glob(os.path.join('examples', '*.py')),
      data_files = [(os.path.join('share', 'doc', PACKAGE_NAME),
                     ['README', 'LICENSE']+glob.glob('doc/*'))],
      )
