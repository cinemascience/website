.. _label_workflow_script:

Custom Script
^^^^^^^^^^^^^

A basic approach is a custom script that generates a database according to the Cinema Specifications, :ref:`label_specifications`.  This approach may be appropriate for both simulation and experimental data, run statistics, or other already extant datasets.  Taking in one CDB, performing analysis and outputting an updated CDB is a common workflow.

Any programming language can be used but here we demonstrate a pandas dataframe approach.  In this pseudo-script, an input CSV file is read in, manipulated, has a final image FILE column added and then is written out to a CDB.  Along the way, the necessary directories are created and the images are moved over from an input directory to the data/image directory.

.. literalinclude:: customCinemaWriter.py
   :language: python
   :lines: 1-

Alternately, one can use a text editor or spreadsheet program to generate the necessary CSV files.

.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CinemaScience website : https://cinemascience.github.io
.. _cinema_view : https://github.com/cinemascience/cinema_view
.. _cinema_explorer : https://github.com/cinemascience/cinema_explorer
.. _CinemaScience Examples : https://cinemascience.github.io/examples.html
.. _ParaView Python Documentation : https://kitware.github.io/paraview-docs/latest/python/quick-start.html
.. _VisIt tutorial: https://wci.llnl.gov/simulation/computer-codes/visit/manuals
.. _ALPINE Ascent: https://alpine-dav.github.io/ascent/

.. toctree::
    :maxdepth: 1
