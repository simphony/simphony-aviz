SimPhoNy Plugin
===============

AViz tools are available in the SimPhoNy library through the
visualisation plug-in named ``aviz``.

e.g::

  from simphony.visualisation import aviz

Visualizing CUDS
----------------

The :func:`~simphony_aviz.show` function is available to
visualise the `Particles` CUDS dataset. The function will open a
AViz and allow the user to view and analyze the particles.

The :func:`~simphony_aviz.snapshot` create a snapshot of
the `Particles` CUDS dataset. The function will create a PNG image
of dataset.

Here is an example illustrating visualizing a particles dataset
in Aviz as well as using the Aviz plugin to take a snapshot:

.. literalinclude:: ../../examples/show_snapshot.py

.. figure:: _images/example_show.png

The different attributes of the particles can be selected in AViz:

.. figure:: _images/example_show_menu.png
