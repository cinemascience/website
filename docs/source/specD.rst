Spec D: Dietrich specification
==============================

The philosophy of Spec D shifted from the global visualization approach of Specs A and C to an *explorer* approach that  leverages the analytic capabilities inherent in 2D+ data abtracts.

Spec D shifts from a JSON-based definition file to a Comma Separate Values (CSV) file.  The first row of the data.csv file is a required row of column headers that are the labels for each column.  Each column represents a data abstract or an (optional) data file such as an image file.  Each row after the header is a data row.  The first data row is required to be non-empty and establishes the data types for each column.  Null and empty values are allowed (after the first data row).  The database can be added to simply by extending the data.csv file.

The additional data files can be of any type, where the format is indicated by MIME name extension.

The Cinema:Explorer Viewer, developed in conjunction with Spec D, provides a parallel coordinate and scatterplot analysis approach.  The user is free to develop other viewers and analysis approaches specific to their data.  The `Cinema Science Github <https://github.com/cinemascience>`_ contains several repositories to support users in developing their own Cinema viewers.  

Detailed Spec D information, in particular the requirements for the data.csv file, can be found in the official write-up: `Dietrich (Spec D) <http://cinemascience.org/wp-content/uploads/sites/13/2017/12/cinema_specD_v011.pdf>`_.



.. toctree::
   :maxdepth: 1
