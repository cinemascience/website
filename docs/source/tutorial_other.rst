.. _label_tutorial_other:

Tutorial: Other Useful information
==================================


.. _label_convert_a2d:

Converting Spec A to Spec D databases
-------------------------------------

It is necessary at times to convert a Spec A to a Spec D Cinema database (CDB).  As of this writing, ParaView v5.6 exports Spec A CDBs (this will be updated to a Spec D export wizard in ParaView v5.7).  Or you may have an older CDB that needs to be updated.

The cinema_lib library can be used to upgrade a Spec A CDB.  Follow the instructions for downloading and installing from the `cinema_lib`_ Github page or see :ref:`_label_cinema_lib`.  Included in that download is a **upgrade_cinema_database** script:

.. code::

  cinema_lib/cinema_lib/upgrade_cinema_database

Simply run the **upgrade_cinema_database** script giving the path to your Spec A database.  This will result in the generation of a Spec D compliant  **data.csv** file.  Once converted, the Spec D CDB can be viewed with your favorite Cinema viewer, :ref:`label_viewers`.

.. code:: bash

    $ upgrade_cinema_database /path_to_database/database_name.cdb

The `CinemaScience GitHub`_ page and the `CinemaScience website`_ are useful sources for more information and ideas.

.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CinemaScience website : https://cinemascience.github.io
.. _cinema_lib : https://github.com/cinemascience/cinema_lib

.. toctree::
   :maxdepth: 2
