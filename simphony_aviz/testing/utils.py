import uuid
import random
import collections

import numpy
from numpy.testing import assert_equal

from simphony.core.keywords import KEYWORDS
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from simphony.cuds.particles import Particle, Bond
from simphony.cuds.mesh import Point, Edge, Face, Cell

try:
    from simphony.cuds.lattice import make_square_lattice
    def dummy_lattice():
        return make_square_lattice('test', 0.2, (10, 10), origin=(0.2, -2.4))
except ImportError:
    from simphony.cuds.lattice import make_cubic_lattice
    def dummy_lattice():
        return make_cubic_lattice('Lattice0', 0.2, (5, 5, 5))

def create_lattice():
    """ Creates lattice 
        
        Creates lattice for testing purposes

    """
    return dummy_lattice()
