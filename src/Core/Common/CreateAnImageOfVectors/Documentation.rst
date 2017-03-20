Create An Image Of Vectors
==========================

.. index::
   single: Vector
   single: Image

Synopsis
--------

This example illustrates how to instantiate and use an *itk::Image* whose pixels are of *itk::Vector* type.


Results
-------
::

  C++

  [1.345, 6.841, 3.295]

  Python

  itkVectorF3 ([1.345, 6.841, 3.295])

Code
----

C++
...

.. literalinclude:: Code.cxx
   :lines: 18-

Python
......

.. literalinclude:: Code.py
   :lines: 1, 20-


Classes demonstrated
--------------------

.. breathelink:: itk::Vector
.. breathelink:: itk::Image