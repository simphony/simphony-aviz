
Simphony-Aviz 
-------------

A visualisation wrapper for the SimPhoNy-framework (http://www.simphony-project.eu/) to provide
visualisation support of the CUDS high-level components.

.. image:: https://travis-ci.org/simphony/simphony-aviz.svg?branch=master
  :target: https://travis-ci.org/simphony/simphony-aviz
  :alt: Build status

.. image:: http://codecov.io/github/simphony/simphony-aviz.svg?branch=master
  :target: http://codecov.io/github/simphony/simphony-aviz?branch=master
  :alt: Test coverage

.. image:: https://readthedocs.org/projects/simphony-aviz?version=stable
  :target: https://readthedocs.org/projects/simphony-aviz?badge=stable
  :alt: Documentation Status


Repository
----------

Simphony-aviz is hosted at: https://github.com/simphony/simphony-aviz

Requirements
------------

- Aviz  (https://github.com/simphony/Aviz)
- simphony >= 0.2.0

Optional Requirements
---------------------

For testing of simphony-aviz, the following is required:
- PIL

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

To run the full test-suite run::

 python -m unittest discover

Usage
------
After installation the user should be able to import and use the ``aviz`` visualisation plugin module for
visualizing with AViz::

  from simphony.visualisation import aviz
      aviz.show(my_particles)

or to create snapshot with AViz::

  from simphony.visualisation import aviz
      aviz.snapshot(my_particles, "snapshot.png")
