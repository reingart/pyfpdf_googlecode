#!/usr/bin/env python

from distutils.core import setup

import sys

import fpdf
package_dir = 'fpdf'
    
setup(name='fpdf',
      version=fpdf.__version__,
      description='Simple PDF generation for Python',
      long_description=open('README.rst').read(),
      author='Olivier PLATHEY ported by Max',
      author_email='maxpat78@yahoo.it',
      maintainer = "Mariano Reingart",
      maintainer_email = "reingart@gmail.com",
      url='http://code.google.com/p/pyfpdf',
      license='LGPLv3+',
      download_url="https://github.com/reingart/pyfpdf/tarball/%s" % fpdf.__version__,
      packages=['fpdf', ],
      package_dir={'fpdf': package_dir},
      package_data={'fpdf': ['font/*.ttf', 'font/*.txt']},
      include_package_data=True,
      classifiers = [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.5",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: PHP Classes",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Multimedia :: Graphics",
      ],
      keywords=["pdf", "unicode", "png", "jpg", "ttf"],
     )

