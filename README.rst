
Simphony-Aviz 
-------------

A visualisation wrapper for the SimPhoNy-framework (http://www.simphony-project.eu/) to provide
visualisation support of the CUDS high-level components.

.. image:: https://travis-ci.org/simphony/simphony-aviz.svg?branch=master
  :target: https://travis-ci.org/simphony/simphony-aviz
  :alt: Build status

.. image:: http://codecov.io/github/simphony/simphony-aviz/coverage.svg?branch=master
  :target: http://codecov.io/github/simphony/simphony-aviz?branch=master
  :alt: Coverage status

.. image:: https://readthedocs.org/projects/simphony-aviz/badge/?version=master
  :target: https://readthedocs.org/projects/simphony-aviz?badge=master
  :alt: Documentation Status


Repository
----------

Simphony-aviz is hosted at: https://github.com/simphony/simphony-aviz

Requirements
------------

- Aviz  (https://github.com/simphony/Aviz)
- simphony ~= 0.5
- pyyaml >= 3.11

Optional Requirements
---------------------

For testing of simphony-aviz, the following is required:
- Pillow

To support the documentation built you need the following packages:

- sphinx >= 1.3.1
- mock

Installation
------------

The package requires python 2.7.x, installation is based on setuptools::

  # build and install
  python setup.py install

or::

  # build for in-place development
  python setup.py develop

Testing
-------

To run the full test-suite::

  python -m unittest discover

Documentation
-------------

To build the documentation::

  python setup.py build_sphinx


Usage
------
After installation the user should be able to import and use the ``aviz`` visualisation plugin module for
visualizing with AViz::

  from simphony.visualisation import aviz
      aviz.show(my_particles)

or to create snapshot with AViz::

  from simphony.visualisation import aviz
      aviz.snapshot(my_particles, "snapshot.png")
