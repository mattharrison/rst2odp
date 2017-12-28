.. include:: <s5defs.txt>

Title
-----

hello world


Code
------

c-like

.. code-block:: pycon

  >>> "%s %s" %('hello', 'world')
  'hello world'

PEP 3101 adds ``.format`` method

.. code-block:: pycon

  >>> "{0} {1}".format('hello', 'world')
  'hello world'


Link Color
----------

.. urlcolor: #008777

http://unicode.org has code charts that map letters to a Unicode *character code*. Currently mapping 110K


Sub/super script
-----------------

Java `TM`:sup:

Sub `text`:sub:

2 handout para
------------------

Pellentesque *dapibus suscipit* ligula.  Donec posuere augue in quam.
Etiam vel **tortor sodales tellus** ultricies commodo.  Suspendisse
potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam,
dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam
laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.
Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.
Vestibulum convallis, lorem a tempus semper, dui dui euismod elit,
vitae placerat urna tortor vitae lacus.  Nullam libero mauris,
consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt
felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a
rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo
sit amet elit.

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.
Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse
potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam,
dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam
laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.
Integer placerat tristique nisl.  Praesent augue.  Fusce commodo.
Vestibulum convallis, lorem a tempus semper, dui dui euismod elit,
vitae placerat urna tortor vitae lacus.  Nullam libero mauris,
consequat quis, varius et, dictum id, arcu.  Mauris mollis tincidunt
felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a
rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo
sit amet elit.


.. class:: handout

  Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.
  Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse
  potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam,
  dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.
  Etiam laoreet quam sed arcu.  Phasellus at dui in ligula mollis
  ultricies.  Integer placerat tristique nisl.  Praesent augue.  Fusce
  commodo.  Vestibulum convallis, lorem a tempus semper, dui dui
  euismod elit, vitae placerat urna tortor vitae lacus.  Nullam libero
  mauris, consequat quis, varius et, dictum id, arcu.  Mauris mollis
  tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis,
  risus a rhoncus fermentum, tellus tellus lacinia purus, et dictum
  nunc justo sit amet elit.  Paragraph 1

  Paragraph 2

  Paragraph 3

Declarations of abbreviations show up in the output
---------------------------------------------------

.. |reST| replace:: reStructuredText

Yes, |reST| is a long word, so I can't blame anyone for wanting to
abbreviate it.


2 para
-------

Hello

World

From script
------------

Make file ``hello.py`` with ::

  print "hello world"

Run with::

  python hello.py

``id``
--------

.. code-block:: pycon

  >>> a = 4
  >>> id(a)

Columns
------------

..  column: 4,2x3

Column 2x3 pos 4

..  column: 1,2x3

Column 2x3 pos 1

Foo bar baz

..  column: 6,2x3

Column 2x3 pos 6

In Git 2.0, Git will default to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

Quote
-----

  Aliquam erat volutpat.  Nunc eleifend leo vitae magna.  In id erat
  non orci commodo lobortis.  Proin neque massa, cursus ut, gravida
  ut, lobortis eget, lacus.  Sed diam.  Praesent fermentum tempor
  tellus.  Nullam tempus.  Mauris ac felis vel velit tristique
  imperdiet.  Donec at pede.  Etiam vel neque nec dui dignissim
  bibendum.  Vivamus id enim.  Phasellus neque orci, porta a, aliquet
  quis, semper a, massa.  Phasellus purus.  Pellentesque tristique
  imperdiet tortor.  Nam euismod tellus id erat.

  --lorem master

Default Image
------------------------

.. image:: snakes.jpg


Fit whole Image on slide
------------------------

.. class:: fit

  .. image:: snakes.jpg

Crop Image on slide
------------------------

.. class:: crop

  .. image:: snakes.jpg

Fill Image on slide
------------------------

.. class:: fill

  .. image:: snakes.jpg

Font
----

.. role:: Alegreya

.. font: alegreya|{"fo:font-family": "Alegreya"}

.. role:: alegreya

This :Alegreya:`should be in alegreya font!`

:orange:`text`

Outside font

.. role:: c64

.. font: c64|{"fo:font-family": "Commodore 64"}

Here is some text with :c64:`retro font`

.. push fo:font-family push_style(TextStyle({'fo:font-family': name

.. drawing-page-properties: {"draw:fill-color":"#772953"}

Tweaking Frame Properties
-------------------------

.. graphic-properties: CLASSNAME {"draw:fill-color":"#112953", "draw:opacity":"50%", "draw:fill":"solid"}

.. graphic-properties: CLASSNAME2 {"draw:fill-color":"#11aa53", "draw:opacity":"50%", "draw:fill":"solid"}

.. paragraph-properties: CLASSNAME {"fo:margin-left":"3cm", "fo:margin-right":"3cm", "fo:margin-top":"1cm"}

.. class:: classname

   Should have blue background

.. class:: classname2

   Should have blue background

Some more stuff
