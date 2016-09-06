===================
Table Test
===================



Basic
--------------


+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+

..
..      Basic 2
..      ----------------
..
..      =====  =====  ======
..        A      B    A or B
..      =====  =====  ======
..      False  False  False
..      True   False  True
..      False  True   True
..      True   True   True
..      =====  =====  ======
..
..      Table Directive
..      ---------------
..
..
..      .. table:: Truth table for "not"
..
..         =====  =====
..           A    not A
..         =====  =====
..         False  True
..         True   False
..         =====  =====

Complicated Table Directive
---------------------------

.. table:: Frozen Delights!
   :class: tufte

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   2      3
       4      5
   =====  =====

Test
-----

Before

=========== ==========
A           B
=========== ==========
1           2
2           3
=========== ==========

After
