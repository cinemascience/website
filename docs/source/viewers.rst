.. _label_viewers:

CinemaScience Viewers
======================

CinemaScience provides reference viewers and flexible components for users to build application specific viewers.  The basic viewers are introduced here.  A full viewer tutorial is available at  :ref:`label_tutorial_viewers`.

.. _label_cinema_compare:

CinemaCompare
-------------

**CinemaCompare** is an interactive visualization approach to exploring Spec D Cinema databases.  It can be used with single databases to rotate around a visualization as with the MPAS-Ocean simulation.

.. image:: images/CinemaCompareMPAS.png
   :width: 97%
   :alt: MPAS image
   :align: left

**CinemaCompare** can also be used to compare multiple databases as with this Warp plasma accelerator visualization that compares (left) isosurfaces found with a topological analysis versus (right) isosurfaces based on regular spacing.

.. image:: images/CinemaCompareWarp.png
   :width: 97%
   :alt: Warp image
   :align: left

CinemaCompare can be found at `cinema_compare`_ and its tutorial is at  :ref:`label_tutorial_compare`.

.. _label_cinema_explorer:

CinemaExplorer
--------------

**CinemaExplorer** is a browser based viewer for Spec D databases.  It includes a parallel coordinates view and a scatterplot view. The columns are the data artifacts or derived quantities that are defined in the data.csv file for the Spec D database.  This example is shows the dark matter density from the Nyx cosmological simulation.  Note how one can choose a subset of the images to view by selecting a region along one of the variable axes.

.. image:: images/NyxExplorer.png
    :width: 97%
    :alt: Cinema Explorer Example
    :align: left

CinemaExplorer can be found at `cinema_explorer`_ and its tutorial is at  :ref:`label_tutorial_explorer`.

.. _label_cinema_scope:

CinemaScope
-----------

**CinemaScope** is a prototype multi-platform viewer application that allows the user to interactively explore a Cinema database of images, through both sliders and mouse controls.  CinemaScope is compatible with Sped C CDBs.  In this image, a Sedov blast wave is viewed in CinemaScope.

.. image:: images/cs_sedov.png
    :width: 97%
    :alt: Cinema Scope Example
    :align: left

CinemaScope can be found at `cinema_scope`_ and its tutorial is at  :ref:`label_tutorial_scope`.

Other Viewers
-------------

The `CinemaScience GitHub`_ page contains other Cinema viewers and modules that provide useful examples for developers.  In particular, `cinema_components`_ provides a javascript library of components that can be used to extend CinemaExplorer or individually assembled to create an application-specific viewer (see :ref:`label_cinema_components`).

The Cinema viewer projects include:

- `cinema_components`_ A javascript library containing prebuilt components for viewing and querying Cinema SpecD databases.
- `cinema_newsfeed`_ A pipeline approach to present analysis results to the user.
- `cinema_quest`_ An interactive visual tool for querying Cinema Database ensembles.
- `cinema_bandit`_ A multi-view application for analysis and visualization of experimental data.
- `cinema_debye_scherrer`_ An interactive web-based tool to visualize multiple datasets.
- `cinema_simpleviewers`_ A set of simple viewers to be used as examples to create custom Cinema viewers.
- `cinema_unityviewer`_ An experimental viewer based on the Unity game engine.


.. _cinema_compare : https://github.com/cinemascience/cinema_compare
.. _cinema_explorer : https://github.com/cinemascience/cinema_explorer
.. _cinema_scope : https://github.com/cinemascience/cinema_scope
.. _CinemaScience GitHub : https://github.com/cinemascience
.. _cinema_components :  https://github.com/cinemascience/cinema_components
.. _cinema_newsfeed :  https://github.com/cinemascience/cinema_newsfeed
.. _cinema_quest : https://github.com/cinemascience/cinema_quest
.. _cinema_bandit : https://github.com/cinemascience/cinema_bandit
.. _cinema_debye_scherrer : https://github.com/cinemascience/cinema_debye_scherrer
.. _cinema_simpleviewers : https://github.com/cinemascience/cinema_simpleviewers
.. _cinema_unityviewer : https://github.com/cinemascience/cinema_unityviewer

.. toctree::
   :maxdepth: 2
