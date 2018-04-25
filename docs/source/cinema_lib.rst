cinema_lib
==========

*cinema_lib* is a set of tools and library for interacting with a Cinema database (currently Spec A and Spec D) through Python and the command line tool, *cinema*.

To run the command line tool directly from the repository, after cloning:

::

  $ git clone https://github.com/cinemascience/cinema_lib.git
  $ cd cinema_lib
  $ ./cinema

To install with *pip*:
::

  $ git clone https://github.com/cinemascience/cinema_lib.git
  $ cd cinema_lib
  $ pip install .
  $ cinema

Minimum requirements are:
  - Python 3.6

Optional requirements are:
  - numpy >=1.13
  - image capabilities
  - OpenCV capabilities
  - scikit-image >=0.13.1
  - image capabilities
  - opencv-python >=3.4
  - OpenCV capabilities

Functionality
-------------

Usage
+++++

::

  cinema [-h] [--version] [-v] [-q] [-a DB] [-d DB] [-l STR] [-t] [-i]
              [--a2d] [--d2s] [--s2d DB] [--image-grey N] [--image-mean N]
              [--image-stddev N] [--image-unique N] [--image-entropy N]
              [--image-joint N] [--image-canny N] [--image-firstq N]
              [--image-secondq N] [--image-thirdq N] [--image-90th N]
              [--image-95th N] [--image-99th N]

Optional Arguments
+++++++++++++++++++

-h, --help
  show this help message and exit
--version
  show program's version number and exit
-v, --verbose
  FLAG: report verbosely
-q, --quick
  FLAG: do not validate row data, if validating (--test)
-a DB, --astaire DB
  INPUT: specify an input Spec A database
-d DB, --dietrich DB
  INPUT: specify an input Spec D database
-l STR, --label STR
  INPUT: specify a header (label) for new output columns, otherwise a default label is generated. if the column(s) are output files, FILE will be automatically prepended to the supplied label.
-t, --test
  VALIDATE: validate input databases. if used in combination with a COMMAND, will only continue processing if INPUT databases are valid
-i, --info
  VALIDATE: report the header (parameters) of the database
--a2d, --astairetodietrich
  COMMAND: convert a Spec D database to a Spec A database, in place
--d2s, --dietrichtosqlite
  COMMAND: create a SQLite3 database from a Spec D database, to ./<database_name>.sqlite
--s2d DB, --sqlitetodietrich
  DB COMMAND: create a a Spec D database CSV from a SQLite database. If there is only one table, it converts that table, otherwise it converts a table or view named "cinema".
--image-grey N
  COMMAND: convert and write image data to greyscale PNG in column number N, using scikit-image color.rgb2grey. new files are named "<old_base_filename>_image_grey.png"
--image-mean N
  COMMAND: add image mean data calculated from images in column number N
--image-stddev N
  COMMAND: add image standard deviation data calculated from images in column number N
--image-unique N
  COMMAND: add unique pixel count data calculated from images in column number N
--image-entropy N
  COMMAND: add image Shannon entropy data calculated from images in column number N, using a histogram with 131072 bins
--image-joint N
  COMMAND: add the joint entropy (multi-dimensionalShannon entropy) data calculated from images in columnnumber N, using 1024 discretization levels per dimension
--image-canny N
  COMMAND: add Canny edge pixel count data calculated from images in column number N
--image-firstq N
  COMMAND: add the first quartile data calculated fromimages in column number N
--image-secondq N
  COMMAND: add the second quartile data calculated fromimages in column number N
--image-thirdq N
  COMMAND: add the third quartile data calculated from images in column number N
--image-90th N
  COMMAND: add the 90th percentile data calculated from images in column number N
--image-95th N
  COMMAND: add the 95th percentile data calculated fromimages in column number N
--image-99th N
  COMMAND: add the 99th percentile data calculated fromimages in column number N

Notes
+++++

- Column numbers, N, are 0-indexed, i.e., 0, 1, 2, etc.
- Only one COMMAND can be run at a time.
- VALIDATE and FLAG can be run in conjunction with COMMAND or run independently.
- Image functions require that the input database is Spec D. The database
  (data.csv) will be backed up prior to running the command. Backup files
  can be found in the database directory as "data_csv.<timestamp>.<md5 hash>".
- Images in a column need to have the same number of components (grey, rgb, rgba, etc.) and that there is an image file in the first data row to be able to detect the number of components for the images.
- Functions run on multi-component images will operate per component,
  returning the result per component, except for --image-unique and
  --image-joint.

Examples
++++++++

Validate a Spec A database:

::

  $ cinema -t -a cinema_lib/test/data/sphere.cdb

Return the header (parameters, columns) for a Spec D database:

::

  $ cinema -i -d cinema_lib/test/data/sphere.cdb

Quickly validate a Spec D database and report the header, verbosely:

::

  $ cinema -itvq -d cinema_lib/test/data/sphere.cdb

Validate a Spec A database and convert it to a Spec D database:

::

  $ cinema -t --a2d -a cinema_lib/test/data/sphere.cdb

Convert RGB images to greyscale images:

::

  $ cinema -d cinema_lib/test/data/sphere.cdb --image-grey 2

Calculate the average color per component in images, naming the column *average*:

::

  $ cinema -d cinema_lib/test/data/sphere.cdb --image-mean 2 --label average
