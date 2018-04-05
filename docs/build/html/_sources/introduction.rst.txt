What is Cinema?
===============

Cinema is an innovative way of capturing, storing, and exploring extreme scale scientific data -- either simulation data or experimental data. It is a highly interactive image-based approach to data analysis and visualization that promotes flexible investigation of large scientific datasets.

Scientific data, simulation or experimental, is usually a 3D representation of some phenomenon.  Cinema provides a way to abstract that 3D data into a "2D+" image-based representation.   This image-based approach encompasses the traditional concept of an image as a 2D picture.  This image might be a visualization rendered from a simulation or it could be an image resulting from a visual-based detector (e.g., X-ray diffraction).  But the image concept can be extended from a simple 2D representation to a 2D+ representation by saving a wide range of information abstracted from the data.  For example, instead of saving a single colormapped variable at a single pixel, Cinema can be used to save a series of floating point variables associated with each pixel in the image.  The resultant Cinema database thus contains multiple raw data variables that can be directly accessed for rendering and analysis.

Cinema enables a multitude of analysis approaches.  At the simplest level, a Cinema viewer can be used to visualize a Cinema database, exploring the data as if one were using the original 3D representation -- but rendering the visualization much faster than possible on the full 3D simulation.  Beyond exploring the data, sophisticated analysis algorithms can be applied to the saved raw data variables.  The results of that analysis could be a new visualization or it could be a single measurement abstracted from the data at each time step.  Computer vision techniques can be used on the raw data to detect, measure, and track features in the data, revealing the scientifically meaningful temporal or spatial evolution of those features.  Image processing techniques can be applied to clean up noisy experimental images.  Change detection techniques can be used to identify interesting time steps or spatial regions of a simulation.  Cinema can also be used to curate parameters from experimental or simulation runs.  Used in conjunction with analysis approaches, the scientist can explore and identify run parameters of particular interest, potentially saving time spent on experimental runs or driving the next round of simulation runs.

The bounds of data exploration with Cinema are limited only by one's imagination.  Details of the Cinema database Specification versions are in Specifications and the Cinema Viewers are described in Viewers.  Each Viewer has a tutorial to quickly come up to speed on its use.

Cinema is developed by the `Data Science at Scale Team <https://www.dsscale.org>`_  at `Los Alamos National Laboratory <https://www.lanl.gov>`_.

All of our software is open source, and is available at the `Cinema Science github page <https://github.com/cinemascience>`_.  We invite the community to contribute code, documentation, examples, bug fixes, etc.  Simply issue a pull request.


.. toctree::
   :maxdepth: 1
