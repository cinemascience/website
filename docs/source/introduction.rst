.. _label_introduction:

What is Cinema?
===============

Cinema is an innovative way of capturing, storing, and exploring extreme scale scientific data -- either simulation data or experimental data. It is a highly interactive approach to data analysis and visualization that promotes flexible investigation of large scientific datasets.  The Cinema ecosystem consists of database specifications, writers, viewers, and algorithms.  Cinema databases consist of data abstracts that are accessed via Cinema viewers in a browser-based approach.  While earlier versions of Cinema focussed on images, the current version of Cinema expands the concept of data abstracts to include images, variables, parameters, metadata, mesh files, and csv files.

Cinema enables a multitude of analysis approaches.  At the simplest level, a Cinema viewer can be used to visualize a Cinema database, exploring the data through pre-rendered images as if one were using the original 3D representation -- but rendering the visualization much faster than possible on a full 3D simulation.  Beyond exploring the data, sophisticated analysis algorithms can be applied to the saved raw data variables.  The results of that analysis could be a new visualization or it could be a single measurement abstracted from the data at each time step.  Computer vision techniques can be used on the raw data to detect, measure, and track features in the data, revealing the scientifically meaningful temporal or spatial evolution of those features.  Image processing techniques can be applied to clean up noisy experimental images.  Sampling or change detection techniques can be used to identify interesting time steps or spatial regions of a simulation.  Cinema can also be used to curate parameters from experimental or simulation runs.  Used in conjunction with analysis approaches, the scientist can explore and identify run parameters of particular interest, potentially saving time spent on experimental runs or driving the next round of simulation runs.

Cinema writers are available through common visualization applications.  A Cinema database export wizard is accessible interactively in `ParaView`_ and will be available in the upcoming `VisIt`_ release.  Or a Cinema database can be produced through ParaView's Catalyst or VisIt's LibSim in situ libraries.  The `Ascent`_ infrastructure can also be used to export Cinema databases.  A Cinema python library, cinema_lib, a command line tool is also available.  Lastly,  application-specific writers to create Cinema databases are also straightforward to implement in Python or other scripting languages.

The bounds of data exploration with Cinema are limited only by one's imagination.  Details of the Cinema database Specification is in Specifications and the Cinema Viewers are described in Viewers.

Cinema is developed by the `Data Science at Scale Team`_  at `Los Alamos National Laboratory`_.

All of our software is open source, and is available at the `CinemaScience GitHub`_  page.  We invite the community to contribute code, documentation, examples, bug fixes, etc.  Simply issue a pull request.

.. _ParaView : https://www.paraview.org/
.. _VisIt : https://wci.llnl.gov/simulation/computer-codes/visit
.. _Ascent : https://alpine-dav.github.io/ascent/
.. _Data Science at Scale Team : https://dsscale.org
.. _Los Alamos National Laboratory :  https://www.lanl.gov
.. _CinemaScience GitHub : https://github.com/cinemascience

.. toctree::
   :maxdepth: 1
