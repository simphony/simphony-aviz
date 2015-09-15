from simphony.cuds.abc_particles import ABCParticles
from simphony.cuds.abc_lattice import ABCLattice
from simphony.cuds.abc_mesh import ABCMesh

from simphony_aviz.util import (temp_particles_filename,
                                convert_particles_to_input_file,
                                run_aviz)


def show(cuds):
    """ Show a CUDS container.

    Parameters
    ----------
    cuds : {ABCMesh, ABCParticles, ABCLattice}
        The CUDS dataset to be shown.

    Raises
    ------
    TypeError:
        If the container type is not supported by the engine.

    """
    if isinstance(cuds, ABCParticles):
        with temp_particles_filename() as filename:
            convert_particles_to_input_file(cuds, filename)
            run_aviz(filename)
    elif isinstance(cuds, ABCLattice) or isinstance(cuds, ABCMesh):
        raise TypeError("Only Particles can be shown by AViz")
    else:
        msg = 'Provided object {} is not of any known cuds type'
        raise TypeError(msg.format(type(cuds)))
