.. _label_cinemasci:

Cinemasci Python Toolkit
========================

*cinemasci* is a set of python tools for reading, writing and viewing Cinema databases

Requirements
------------

Minimum Requirements are:

- ``Python 3.7`` or above

This project uses coding standards spelled out in `PEP8`_.

Installation
------------

The cinemasci module is available on the `CinemaScience GitHub`_: at `cinemasci`_.  It can be installed in multiple ways.

Clone the repository:

.. code:: bash

  $ git clone --recurse-submodules https://github.com/cinemascience/cinemasci.git

  or

  $ git clone https://github.com/cinemascience/cinemasci.git
  $ cd cinemasci
  $ git submodule init
  $ git submodule update


Alternately, the latest release of this module is available on pypi.org, and can be installed with ``pip``:

.. code:: bash

  $ pip install cinemasci

Or it can be installed locally from source using the ``setup.py`` file.

Cinemasci submodules
--------------------

The ``cinemasci`` submodules are used for common Cinema tasks:

    * ``cdb``: Tools for reading, writing and manipulating a cinema database.
    * ``cis``: Tools for reading, writing and manipulating composable image sets.
    * ``pynb``: A Jupyter notebook viewer for simple databases.
    * ``server``: A simple server to help view databases, using the viewers submodule.
    * ``viewers``: Viewers (submodule)

Please see the cinemasci tutorial, :ref:`label_tutorial_cinemasci`, for examples of using Cinemasci functionality.


.. _CinemaScience GitHub : https://github.com/cinemascience
.. _cinemasci : https://github.com/cinemascience/cinemasci
.. _PEP8 : https://www.python.org/dev/peps/pep-0008/

.. toctree::
   :maxdepth: 2
