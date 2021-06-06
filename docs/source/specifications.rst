.. _label_specifications:

CinemaScience Specifications
============================

A Cinema database is a collection of data extracts that can be accessed for visualization or interactive data exploration via a viewer application.

* `Spec D`_ : With Cinema release v1.3 and later, Cinema converged on a specification, :ref:`label_specD`, that incorporates the flexibility and functionality of previous releases while expanding the Cinema data specifications.  Official `Release Notes`_ are available on the `CinemaScience GitHub`_ page.  This  specification includes multiple files per database entry and arbitrary data.  It has a suite of flexible viewers and view components for a wide range of analysis approaches.

* `CIS`_ : A second specification is the new Composable Image Set specification, :ref:`label_cis`, that supports advanced and flexible post hoc colormapping.



.. _Spec D : https://github.com/cinemascience/cinema/blob/master/specs/dietrich/01/cinema_specD_v012.pdf
.. _Release Notes : https://github.com/cinemascience/cinema/blob/master/doc/release/1.3/notes.md
.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CIS : https://github.com/cinemascience/design

.. toctree::
   :maxdepth: 2

   specD
   cis_design
   specAC
