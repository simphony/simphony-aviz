import contextlib
import os
import shutil
import tempfile

from simphony.core.cuds_item import CUDSItem


@contextlib.contextmanager
def temp_particles_filename():
    """ Context manager provides temporary file

    Temporary file (and the directory it is in) will
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
        output_file.write("#XZYfile\n")
        for particle in particles.iter_particles():
            dummy_type = "cc"
            output_file.write(
                "{0} {1[0]:.16e} {1[1]:.16e} {1[2]:.16e}\n".format(
                    dummy_type,
                    particle.coordinates))
