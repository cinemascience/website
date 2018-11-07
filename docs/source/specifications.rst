.. _label_specifications:

CinemaScience Specifications
============================

A Cinema database is a collection of data abstracts that can be accessed for visualization or interactive data exploration via a viewer application.

Current Specification: Spec D
-----------------------------

With the latest Cinema release v1.3, Cinema has converged on a single specification, Spec D, that incorporates the flexibility and functionality of previous releases while expanding the Cinema data specifications.  Official `Release Notes`_ are available on the `CinemaScience GitHub`_ page.

* `Dietrich (Spec D)`_ : This updated specification includes multiple files per database entry and arbitrary data.  It has a suite of flexible viewers and view components for a wide range of analysis approaches.

The workflow tutorial, :ref:`label_workflow`, provides detailed ways to produce Cinema databases.

Deprecated Specifications: A & C
--------------------------------

These specifications are no longer supported.

* Astaire (Spec A) : This was a basic embodiment of the original Cinema image-based approach.  It includes both static and spherical cameras, and includes the capability to turn elements on and off as detailed in the SC paper. The resulting Spec A database is a colormapped visualization that can be viewed interactively with a standalone application viewer.
* Chaplin (Spec C) : This specification included mobile cameras, floating point images, and data abstracts, and the ability to change and apply colormaps.


.. _Dietrich (Spec D) : https://github.com/cinemascience/cinema/blob/master/specs/dietrich/01/cinema_specD_v012.pdf
.. _Release Notes : https://github.com/cinemascience/cinema/blob/master/doc/release/1.3/notes.md
.. _CinemaScience GitHub : https://github.com/cinemascience

.. toctree::
   :maxdepth: 2
   :caption: Spec D Details

   specD
