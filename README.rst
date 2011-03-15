===================================
rst2odp: rst to LibreOffice impress
===================================

This package contains a Python script (rst2odp) to convert `reStructuredText
<http://docutils.sourceforge.net/rst.html>`_ to `LibreOffice
<http://www.libreoffice.com>`_ Impress (rst2odp). It also includes a general
python library (``odplib/preso.py``) for creating Impress files.

Installation
============

To build and install this Python package, you will first need to build/install
docutils, pygments, and PIL. After you have done this, follow these steps:

    $ python setup.py install

Usually it is run like so:

    $ rst2odp path/to/rstfile.rst output.odp

(use --traceback -r 3 for debug)

Styling is supported with the ``--template-file`` switch, just pass it an .otp
template file.

TODO
====

* |DONE| Image scaling
* |DONE| Support for background image per slide
* |DONE| Support for no title (transition directive)
* |DONE| Enumerated list
* |DONE| Simple animations
* Fix enumerated lists separated by "\n..\n"
* Auto resize textframes/(images too?) as they are added
* ...

Authors
=======

This project was started by and continues to be led by `Matt Harrison
<https://github.com/mattharrison>`_.

.. |DONE| unicode:: U+2611
