.. _label_cinema_movie:

cinema_movie Tool
=================

*cinema_movie* is a tool to create a movie from a Cinema database (CDB).

Requirements
------------

Minimum Requirements are:

- Python 3.7
- pyyaml, pandas, numpy, opencv-python


Files
-----

.. code::

  simple_movie - main program
  movie.yaml - control file
  cmovie - movie production module

The **simple_movie** script takes in a Cinema database (CDB) and creates a movie based on the primary frame variable within the CDB.  Control is through a human-readable YAML configuration file.  Cinema_movie can be used to create a movie over time for a single static view as defined in the movie.yaml file.  The cmovie module contains the functions needed to create the movie.

Control Parameters: movie.yaml
------------------------------

The yaml control file is used to point to the database and define the parameters to make the movie.


Path and database information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  cdb_path : ./data/
  cdb_name : example_data.cdb

Output movie information
^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  frame_rate : 5.0         # number of frames per second
  movie_name : cinema.mp4  # name of output movie


Variables to define images and static view used in the movie
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

  frame_var   : time        # primary control variable along which movie is made; typically time
  FILE_choice : FILE        # which FILE* column of images to use in making movie
  views :
    phi   : -90
    theta : 0

There are error checks on the path and database name and to verify the database columns that will be used in the movie.  If there are no images found that satisfy the requested movie parameters, a warning message will print.

Usage
-----

Edit the movie.yaml file to point to the CDB, adjust the name of the output movie, choose movie frame rate and the variable along which to make the movie.  Edit the views variable to define the single static view that will be used.  Edit the FILE variable if using a different FILE column of images.

Make a movie by running the script:

.. code::

  $ ./simple_movie



.. toctree::
   :maxdepth: 2
