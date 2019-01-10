.. _label_tools:

CinemaScience Algorithms, Libraries, and Tools
==============================================

CinemaScience includes algorithms, code libraries, and tools to facilitate analysis in situ and postprocessing, available on the `CinemaScience GitHub`_ page. The Cinema algorithm, library, and tool projects include:

- `cinema_change_detection`_ A R command line tool that takes as input a Cinema database and produces a new Cinema database with change detection results using Myers et al. This tool also produces a change detection png image and json file to be used with Cinema:Newsfeed.
- `cinema_asqlpy`_ An apsw/SQLite virtual table interface to Cinema Spec A databases.
- `cvlib`_ A Cinema Viewer library which provides a JavaScript API to Spec A Cinema databases for visualization in the browser.
- `cvlibd`_ A Javascript framework to facilitate development of viewer applications for Spec D Cinema databases in the browser.
- `cinema_lib`_ Python 3.6 library and command line tool for Cinema specifications A and D.

.. _CinemaScience GitHub : https://github.com/cinemascience
.. _cinema_change_detection :  https://github.com/cinemascience/cinema_change_detection
.. _cinema_lib : https://github.com/cinemascience/cinema_lib
.. _cinema_asqlpy : https://github.com/cinemascience/cinema_asqlpy
.. _cvlib : https://github.com/cinemascience/cvlib
.. _cvlibd : https://github.com/cinemascience/cvlibd

.. toctree::
   :maxdepth: 2
   :caption: Libraries

   cinema_lib
   cinema_components
