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


Animated Frames
-----------------

Everything in the animation should appear together on click

.. animation::

  .. grid:: 1,2x1

     .. class:: fit_top_left

        .. image:: img/test.png


  .. textbox:: {"x": "10cm", "y": "12.2cm"}

    Anim Text starting at position 10, 12.2

.. animation::

  .. grid:: 2,2x1

     .. class:: fit_top_left

        .. image:: img/test.png


  .. textbox:: {"x": "20cm", "y": "12.2cm"}

    Anim Text 2 starting at position 10, 12.2


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




Adjusting Images
----------------

.. class:: crop

  .. image:: img/test.png

Using ``.. class:: crop`` fills the screen and crops off extra. Preserving ratios. Note that the title disappears as it is under (z layer) the image.

Adjusting Images
----------------

.. class:: fill

  .. image:: img/test.png

Using ``.. class:: fill`` fills the screen but does not crop any. It might stretch the image

Adjusting Images
----------------

.. class:: fit

  .. image:: img/test.png

Using ``.. class:: fit`` fills the screen but does not crop any.  Preserving ratios.


Adjusting Images with Grids
---------------------------

Put image in a second cell of 3 columns and 1 row

.. grid:: 2,3x1

   .. class:: fit
      
     .. image:: img/test.png


Who Created Python?
-------------------

.. grid:: 1,2x1

   .. class:: fit_top_left

     .. image:: img/test.png


.. grid:: 2,2x1

Python was created by Dutch programmer Guido van Rossum in 1989.
He wanted to create a tool to allow for easy scripting
  


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

Can specify font size
---------------------

.. class:: font-size:100pt

  Large text

Grids
-----


.. grid:: 2,3x1

  Put text in a second cell of 3 columns and 1 row

.. grid:: 4,1x4

  Text along bottow cell of 4 rows

Incremental Text
----------------

Due to "feature" in ODT spec, it only works (by clicks) on a paragraph or outline level.

.. class:: incremental

  * foo
  * bar
  * baz

Hyperlinks
----------


External hyperlinks, like Python_.

.. _Python: http://www.python.org/


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

Font
----

.. role:: Helvetica

.. font: helvetica|{"fo:font-family": "Helvetica"}

.. role:: helvetica

This :Helvetica:`should be in helvetica font!`

Arrow & Textbox
---------------

.. arrow: {"x1":"1cm","y1":"2cm","x2":"10cm","y2":"12cm", "color":"#00ffff", "width":"5pt"}

.. textbox:: {"x": "10cm", "y": "12.2cm"}

  Text starting at position 10, 12.2


Master Pages
-------------

Open(Libre)Office have the notion of Master Pages. If you have a template that has multiple master pages (click on Format -> Slide Design to see the templates. At the bottom is the name). To use a different template for a slide insert::

  .. slide-design:: template-name

*before* a title.

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
