Spec A: Astaire specification
=============================

Spec A is the original *simple* Cinema database specification consisting of:

An image collection sampled by:
  - A single Cinema camera. A Cinema camera can be either static  or spherical, indicating how the camera samples views. The Cinema database is a collection of images for all (time, position) pairings defined by the export script.

  - Zero or one clipping plane operators, with an associated range of clipping values.

  - Zero or one contour operators, and an associated range of contour values.

JSON metadata file
  A JSON file that is a specific instance of one of the Cinema "simple" Database schema.

Together, the image collection and JSON file make up the Cinema *Simple* or *Spec A* database.

*Simple* Schema Definition
--------------------------
The *simple* schema consists of:

Header information
  This is required database header information, and values must be as defined below.



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
  The rest of the file consists of arguments that define the valid values for the variables in the name_pattern files. They have the following form:

::

  <string>: {
  "default": <value>,
  "label": <string>,
  "type": "range",
  "values": [ list of unique values ]
  }

Example: Static database
------------------------
This example is based on the above JSON schema outline.  Because there is no 'phi' or 'theta' value for an
argument, this example shows a static Cinema camera.

::

  {
  "type" : "simple",
  "version" : "1.1",
  "metadata": {
  "type": "parametric-image-stack"
  },
  "name_pattern": "{time}/{slice}.jpg",
  "arguments": {
  "slice": {
  "default": -17.3205,
  "label": "slice",
  "type": "range",
  "values": [
    -17.3205,
    -13.4715,
    -9.6225,
    -5.7735,
    -1.9245,
    1.9245,
    5.7735,
    9.6225,
    13.4715,
    17.3205
    ]
  },
  "time": {
  "default": "0.000000",
  "label": "time",
  "type": "range",
  "values": [
  "0.000000",
  "0.500000"
  ]
  }
  }
  }

.. toctree::
   :maxdepth: 1
