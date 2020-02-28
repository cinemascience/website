.. _label_cinema_movie:

cinema_movie Tool
=================

*cinema_movie* is a tool to create a movie from a Cinema database (CDB).  This is a new functionality currently under development.  Updates on this documentation page may not completely reflect current capabilities.  For the latest information on **cinema_movie**, please check out the README the `cinema_movie GitHub`_ page.

Requirements
------------

Minimum Requirements are:

- Python 3.7
- pandas, numpy, opencv-python


Files
-----

.. code::

  cinema_movie - main program
  cmovie - movie production module

The **cinema_movie** script takes in a Cinema database (CDB) and creates a movie based on the set of frames described in the **frames.csv** control file.   The cmovie module contains the functions needed to create the movie.

Command Line Control Parameters
-------------------------------

A series of command line arguments can be used to modify the functionality of **cinema_movie**:

.. code::

  cdb:    Set input path and Cinema database name (default: ./data/example_data.cdb)
  frames: Set input csv file name to choose views in the movie; assumes path is cdb (default: ./data/example_data.cdb/frames.csv)
  FILE:   Set the image column used from the CDB (default: FILE)
  fps:    Set the frame rate for the movie (default: 5 fps)
  opath:  Set/creates path to output movie (default: ./)
  movie:  Set output movie name (default: cinema.mp4)

There are error checks on the path and database name and to verify the database columns that will be used in the movie.  If there are no images found that satisfy the requested movie parameters, a warning message will print.

Usage
-----

Make a movie by running the script with any modified arguments.  Examples of usage

.. code::

  $ ./cinema_movie
  $ ./cinema_movie --cdb ./tmp/my_cdb.cdb --fps 10 --movie mymovie.mp4



.. _CinemaScience GitHub : https://github.com/cinemascience
.. _CinemaScience website : https://cinemascience.github.io
.. _cinema_movie GitHub: https://github.com/cinemascience/cinema_movie


.. toctree::
   :maxdepth: 2
