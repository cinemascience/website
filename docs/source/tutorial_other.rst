.. _label_tutorial_other:

Tutorial: Other Useful information
==================================


.. _label_convert_a2d:

Converting Spec A to Spec D databases
-------------------------------------

It is necessary at times to convert a Spec A to a Spec D Cinema database (CDB).  Spec A CDBs are available from ParaView v5.6 and earlier, from VisIt, from Ascent or you may have an older CDB that needs to be updated.

The cinema_lib library can be used to upgrade a Spec A CDB.  Follow the instructions for downloading and installing from the `cinema_lib`_ Github page or see :ref:`label_cinema_lib`.  Included in that download is a ``upgrade_cinema_database`` script:

.. code::

  cinema_lib/cinema_lib/upgrade_cinema_database

Simply run the ``upgrade_cinema_database`` script giving the path to your Spec A database.  This will result in the generation of a Spec D compliant  ``data.csv`` file.  Once converted, the Spec D CDB can be viewed with your favorite Cinema viewer, :ref:`label_viewers`.

.. code:: bash

    $ upgrade_cinema_database /path_to_database/database_name.cdb


.. _label_browser_security:

A Note on Browser Security
--------------------------

To use the browser-based viewers, you **MUST** allow local file access. Do this in the following way, but be sure to reset these options when you are done as this allows loading of a file from any folder.

- **Firefox (preferred)**
    - In the brower search bar, enter ``about:config``
    - Set ``privacy.file_unique_origin`` to ``false``
    - Set ``security.fileuri.strict_origin_policy`` to ``false``

- **Safari**
    - Safari->Preferences->Advanced->Show Develop menu in menu bar
    - Safari->Develop->Disable Local File Restrictions (on)

- **Chrome**
    - open **chrome** with the option ``--disable-web-security``
    - Mac example:
        open -na "Google Chrome" cinema_view.html --args --user-data-dir="<path/to/repo>" --disable-web-security

The `CinemaScience GitHub`_ page and the `CinemaScience website`_ are useful sources for more information and ideas.

.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CinemaScience website : https://cinemascience.github.io
.. _cinema_lib : https://github.com/cinemascience/cinema_lib

.. toctree::
   :maxdepth: 2
