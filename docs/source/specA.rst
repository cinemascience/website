Spec A: Astaire specification
=============================

Spec A is the original "simple" Cinema database specification.  A Cinema database is a collection of data that supports an image-based approach to interactive data exploration. It is a set of images and associated metadata.

The "simple" database consists of:

An image collection sampled by:
  - A single Cinema camera. A Cinema camera can be either static  or spherical, indicating how the camera samples views. The Cinema database is a collection of images for all (time, position) pairings defined by the export script.

  - Zero or one clipping plane operators, with an associated range of clipping values.

  - Zero or one contour operators, and an associated range of contour values.

JSON metadata file
  A JSON file that is a specific instance of one of the Cinema "simple" Database schema.

Together, the image collection and JSON file make up the Cinema Spec A database.

Schema Definition
^^^^^^^^^^^^^^^^^
The schema consists of:

Header information
  This is required database header information, and values must be as defined below.

.. highlight:: json
::

  "type" : "simple",
   "version" : "1.1",
   "metadata": {
   "type": "parametric-image-stack"
   },


name_pattern
  This string shows how to construct valid paths to Cinema database images. It must be a path relative to the location of the <database>.json file.

::

  "name_pattern" : <valid file path with substitutions>
   "name_pattern" : "{time}/{phi}/{theta}/image.png" // several subdirectories
   "name_pattern" : "{time}_{phi}_{theta}_image.png" // all images in one directory

arguments
  The rest of the file consists of arguments that define the valid values for the variables in the name_pattern value. They have the following form:


.. toctree::
   :maxdepth: 1
