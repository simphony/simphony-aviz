Simphony-Aviz 
-------------

A visualisation wrapper for the SimPhoNy-framework (http://www.simphony-project.eu/) to provide
visualisation support of the CUDS highlevel components.

.. image:: https://travis-ci.org/simphony/simphony-aviz.svg?branch=master
  :target: https://travis-ci.org/simphony/simphony-aviz
  :alt: Build status

.. image:: http://codecov.io/github/simphony/simphony-aviz.svg?branch=master
  :target: http://codecov.io/github/simphony/simphony-aviz?branch=master
    :alt: Test coverage


Repository
----------

Simphony-aviz is hosted at: https://github.com/simphony/simphony-aviz

Requirements
------------

- Aviz  (https://github.com/simphony/Aviz)
- simphony >= 0.2.0

Optional requirements
---------------------

For testing of simphony-aviz, the following is required:
- pyface

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
After installation the user should be able to import the ``aviz`` visualisation plugin module by::

  from simphony.visualisation import aviz
    aviz.show(cuds)


