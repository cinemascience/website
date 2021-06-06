.. _label_workflow_catalyst:

In Situ via ParaView Catalyst
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ParaView's in situ Catalyst library can be used to output Cinema Spec D databases.  Within ParaView, load the data and create the visualization you wish to generate in situ.

If the ``Export Inspector`` view is not already opened, it can be opened from either the ``View`` menu by selecting ``Export Inspector`` or from the ``Catalyst`` menu by selecting ``Define Exports``.  Set up the Cinema database export as described in the post-processing Cinema ParaView workflow, :ref:`label_workflow_pv57`

- Under ``Image Extracts``, make sure the correct view is selected.
- Select ``Cinema image database (*.cdb)`` and click the checkbox to the right to establish that option.
- Open the ellipses menu to the right of the checkbox to select the Cinema database options via the Save Screenshot menu.
- Under ``Root Directory``, add the complete path and output database name: ``/<path-to-cdb>/test.cdb``.
- From the ParaView ``Catalyst`` menu, select ``Export Catalyst Script`` and enter a location and name for the exported python script.  The exported script can be edited to fine-tune as needed.  This script can then be integrated into an in situ pipeline.

The `ParaView Python Documentation`_ is an excellent source of information on how to create a Catalyst pipeline.


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
