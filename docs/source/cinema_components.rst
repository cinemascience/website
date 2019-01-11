.. _label_cinema_components:

cinema_components Library
=========================

CinemaScience includes a library of viewer components that can be added by the user to create analysis and data specific viewers. These components include:

- **PcoordSVG** -- A component for viewing and browsing a database on a Parallel Coordinates Chart (rendered with SVG).
- **PcoordCanvas** -- A component for viewing and browsing a database on a Parallel Coordinates Chart (rendered with Canvas).

.. image:: images/cc_parallelcoords.png
    :width: 95%
    :alt: parallel coordinates image
    :align: left

- **Glyph** -- A component for viewing data on a Glyph Chart.

.. image:: images/cc_glyph.png
    :width: 95%
    :alt: glyph image
    :align: left

- **ImageSpread** -- A component for viewing image data for a set of data points.

.. image:: images/cc_imagespread.png
    :width: 95%
    :alt:  image spread
    :align: left

- **Query** -- A component that provides an interface for defining a custom data point and querying the database for similar points.

.. image:: images/cc_query.png
    :width: 95%
    :alt: query image
    :align: left

- **ScatterPlotSVG** -- A component for viewing data on a Scatter plot (rendered with SVG).
- **ScatterPlotCanvas** -- A component for viewing data on a Scatter plot (rendered with Canvas).

.. image:: images/cc_scatterplot.png
    :width: 95%
    :alt: scatterplot image
    :align: left

Example Use Case
^^^^^^^^^^^^^^^^

Cinema viewers are JavaScript/HTML/CSS based and use D3 to link data and user actions.  Below is a simple example of a browser page that uses a pcoordSVG component to control the display of an ImageSpread component for a database name **mydata.cdb** located in the same directory:

.. code:: HTML

  <html>
    <head>
	   <!--Import D3-->
	     <script src="lib/d3.min.js"></script>
	   <!--Import Cinema Components Library-->
	    <script src="CinemaComponents.js"></script>
	   <!--Include Component's CSS-->
	    <link rel='stylesheet' href='css/CinemaComponents.min.css'>
    </head>
    <body>
	   <!--The component will be placed inside container-->
	    <div id="pcoord_container" style="width:500px;height:400px;"></div>
	    <div id="spread_container" style="width:100%;height:400px;"></div>
	    <script>
		    var chart, spread;
		    //First create a database
		    var database = new CINEMA_COMPONENTS.Database('mydata.cdb',function() {
			  //This callback function is called when the database has finished loading
			  //Use it to create your components
			  chart = new CINEMA_COMPONENTS.PcoordSVG(document.getElementByID('pcoord_container'), database);
			  spread = new CINEMA_COMPONENTS.ImageSpread(document.getElementByID('spread_container'),database);

			  //Using dispatch events, components can communicate with each other
			  chart.dispatch.on('selectionchange',function(selection) {
				    spread.setSelection(selection);
			  });
		   });
	    </script>
    </body>
  </html>

Full details on the use of cinema_components is on the `cinema_components GitHub`_ page.  

.. _cinema_components GitHub : https://github.com/cinemascience/cinema_components
