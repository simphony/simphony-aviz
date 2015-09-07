Simphony-Aviz 
-------------

A visualization wrapper for the SimPhoNy-framework (http://www.simphony-project.eu/) to provide
visualization support of the CUDS highlevel components.

.. image:: https://travis-ci.org/simphony/simphony-aviz.svg?branch=master
  :target: https://travis-ci.org/simphony/simphony-aviz
  :alt: Build status


Repository
----------

Simphony-aviz is hosted at: https://github.com/simphony/simphony-aviz

Requirements
------------

- Aviz  (https://github.com/simphony/Aviz)
- simphony >= 0.2.0

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

Usuage
------
After installation the user should be able to import the ``aviz`` visualization plugin module by::

  from simphony.visualization import aviz
    aviz.show(cuds)


