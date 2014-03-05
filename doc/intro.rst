.. include:: <s5defs.txt>

=====================
 rst2odp Slide Shows
=====================

:Author: Matt Harrison
:Date:   2008-12-17

Intro to rst and the odp converter

.. class:: handout

  Everything that is in this block will only be in the notes.
  You can put these on each slide.

Simple Slides
-------------

Here's how to make easy slideshows in rst.  Here's a list:

* Part
* of 
* a 
* list

Image
-----

.. image:: img/test.png


--------

.. class:: center huge

A slide with centered, huge text and no title

Source code
-----------

.. code-block:: python

  def foo(bar, baz):
    fizzle(bar, baz)


More Source code
----------------

.. class:: small

    .. code-block:: c

        int
        main(void) {
            printf("Hello, world\n");
            return 0;
        }

Incremental Text
----------------

Due to "feature" in ODT spec, it only works (by clicks) on a paragraph or outline level.

.. class:: incremental

  * foo
  * bar
  * baz
  
Text styling
------------

:tiny:`Some tiny text` (can also do ``small``, ``big``, or ``huge``)

Some *strong text* and **emphasized text**

:orange:`s5defs.txt Colors are also supported`

.. slide-layout:: 2column

Multiple Columns
----------------

This text goes in the first column.

.. column:: 2

This text goes in the second column.

.. column:: 3

This text goes in the third column.

.. slide-layout:: 1column

Creating slides
---------------

* install ``rst2odp``
* plain : ``rst2odp slides.rst output.odp``
* template : ``rst2odp slides.rst --template-file template/darkGradient.otp output.odp``
* fonts : ``rst2odp --font="Droid Sans" --mono-font="Droid Sana Mono" slides.rst output.odp``
* code highlighting style : ``rst2odp --pygments-style=bw slides.rst output.odp``

Thanks
------

Send feedback/suggestions my way

matthewharrison@gmail.com




