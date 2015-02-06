#from distutils.core import setup
from setuptools import setup

from odplib import meta

setup(name="rst2odp",
      version=meta.__version__,
      author=meta.__author__,
      author_email=meta.__email__,
      description="Converter for rst to OpenOffice Impress",
      long_description='''Packacking of rst2odp and opdlib from docutils sandbox.  odplib is a standalone library for creating odp output from python.  rst2odp wraps it for rst users''',
      license='Apache',
      url='https://github.com/mattharrison/rst2odp',
      scripts=["bin/rst2odp", "bin/otptweak", "bin/odpstyles"],
      #package_dir={"odplib":"odplib"},
      install_requires=['docutils >= 0.10', 'pygments >= 1.6',
                        'pillow >= 1.7.8'],
      package_data={'odplib':['data/*.xml']},
      packages=['odplib'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Office/Business'
        ]
)
