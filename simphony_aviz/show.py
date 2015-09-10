import contextlib
import os
import subprocess
import shutil
import tempfile

from simphony.cuds.abc_particles import ABCParticles
from simphony.cuds.abc_lattice import ABCLattice
from simphony.cuds.abc_mesh import ABCMesh
from simphony.core.cuds_item import CUDSItem


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
        filename = "dummy.input"
        with _temp_particles_filename() as filename:
            convert_particles_to_input_file(cuds, filename)
            subprocess.call(["aviz", filename])
    elif isinstance(cuds, ABCLattice) or isinstance(cuds, ABCMesh):
        raise TypeError("Only Particles can be shown by AViz")
    else:
        msg = 'Provided object {} is not of any known cuds type'
        raise TypeError(msg.format(type(cuds)))


@contextlib.contextmanager
def _temp_particles_filename():
    """ Context manager provides temporary file

    Temporary file (and the directory its in) will
    be destroyed after being used
    """
    temp_dir = tempfile.mkdtemp()
    yield os.path.join(temp_dir, "particles.xzy")
    shutil.rmtree(temp_dir)


def convert_particles_to_input_file(particles, filename):
    """ Convert particles dataset to a AViz file

    """
    with open(filename, "w") as output_file:
        output_file.write(
            "{}\n".format(particles.count_of(CUDSItem.PARTICLE)))
        output_file.write("XZYfile\n")
        for particle in particles.iter_particles():
            dummy_type = "cc"
            output_file.write(
                "{0} {1[0]:.16e} {1[1]:.16e} {1[2]:.16e}\n".format(
                    dummy_type,
                    particle.coordinates))
