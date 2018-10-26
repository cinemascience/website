CinemaScience Tutorial: Writers
===============================

This tutorial will help the user explore the CinemaScience ecosystem.  It will explore how to generate or export Cinema databases (CDBs).

The `CinemaScience GitHub`_ page and the `CinemaScience website`_ are useful sources for more information and ideas.

Exporting & Generating Cinema Databases
---------------------------------------

In Situ via ALPINE Ascent
^^^^^^^^^^^^^^^^^^^^^^^^^

In Situ via ParaView Catalyst
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Situ via VisIt LimSim
^^^^^^^^^^^^^^^^^^^^^^^^

PostProcessing via ParaView Cinema Export Wizard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current ParaView release v5.5.2 has a Cinema Export Wizard that outputs Cinema Spec A databases.  These can be converted to Cinema Spec D databases through the cinema_lib command line interface.  The Cinema Spec D export wizard will be included in an upcoming ParaView release.  This tutorial will be updated when that change takes place.

PostProcessing via VisIt Cinema Export Wizard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current VisIt release v2.13.2 does not yet include the Cinema Export Wizard.  The Cinema Spec D export wizard will be included in the upcoming VisIt release v3.0 (scheduled for Fall 2018).  This tutorial will be updated when that change takes place.

Custom Script
^^^^^^^^^^^^^
A final approach is a custom script to generate a database.  This may be useful for experimental data, run statistics, or other already extant datasets.  Pandas dataframes provide an efficient approach.  In this psuedo script, an input csv file is read in, manipulated, has a final image FILE column added and then is written out to a CDB.  Along the way, the necessary directories are created and the images are moved over from an input directory to the data/image directory.

.. literalinclude:: customCinemaWriter.py
   :language: python
   :lines: 1-


.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CinemaScience website : https://cinemascience.github.io
.. _cinema_compare : https://github.com/cinemascience/cinema_compare
.. _cinema_explorer : https://github.com/cinemascience/cinema_explorer
.. _CinemaScience Examples : https://cinemascience.github.io/examples.html

.. toctree::
   :maxdepth: 2
