import os
import shutil

from simphony.cuds.abc_particles import ABCParticles
from simphony.cuds.abc_lattice import ABCLattice
from simphony.cuds.abc_mesh import ABCMesh

from simphony_aviz.util import (run_aviz,
                                temp_particles_filename,
                                create_xyz_file)


def snapshot(cuds, filename):
    """ Save a snapshot of the cuds object using the default visualisation.

    Parameters
    ----------
    cuds : {ABCMesh, ABCParticles, ABCLattice}
        The CUDS dataset to be shown.
    filename : string
        The filename to use for the output file.

    Raises
    ------
    TypeError:
        If the container type is not supported by the engine.

    """
    if isinstance(cuds, ABCParticles):
        with temp_particles_filename() as temp_xyz_filename:
            create_xyz_file(cuds, temp_xyz_filename)
            run_aviz([temp_xyz_filename, "-snapq"])
            snapshot_dir = os.path.dirname(os.path.realpath(temp_xyz_filename))
            snapshot_file = _find_png(snapshot_dir)
            shutil.copyfile(snapshot_file, filename)
    elif isinstance(cuds, ABCLattice) or isinstance(cuds, ABCMesh):
        raise TypeError("Only Particles can be shown by AViz")
    else:
        msg = 'Provided object {} is not of any known cuds type'
        raise TypeError(msg.format(type(cuds)))


def _find_png(directory):
    """ Return the filename of the first found png file

    Parameters
    ----------
    directory: string
        the directory where pngs are searched for

    """
    for filename in os.listdir(directory):
        name, file_extension = os.path.splitext(filename.lower())
        if file_extension == ".png":
            return os.path.join(directory, filename)
    else:
        raise RuntimeError("Could not find created snapshot")
