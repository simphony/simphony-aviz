import contextlib
import errno
import os
import shutil
import subprocess
import tempfile
import yaml
import numpy
from collections import namedtuple
from itertools import islice

from simphony.core.cuba import CUBA
from simphony.core.cuds_item import CUDSItem
from simphony.core.keywords import KEYWORDS


def run_aviz(command_line_arguments=None, aviz="aviz"):
    """ Run aviz as a subprocess

    Parameters
    ----------
    command_line_arguments : (list of) command line argument(s)
        the arguments to give to aviz
    aviz : str
        path to aviz or name of aviz executable in path

    Raises
    ------
    RuntimeError
        if there is a problem running (i.e. finding) the aviz executable
    """
    aviz_path_and_args = [aviz]
    if command_line_arguments:
        if type(command_line_arguments) is not list:
            aviz_path_and_args.append(command_line_arguments)
        else:
            aviz_path_and_args.extend(command_line_arguments)

    try:
        subprocess.check_call(aviz_path_and_args)
    except OSError as error:
        if error.errno == errno.ENOENT:
            msg = "Problem running Aviz. Ensure that the Aviz executable"
            msg += " (named 'aviz') can be found in your PATH. "
            msg += " (errno={}, stderror={})".format(error.errno,
                                                     error.strerror)
            raise RuntimeError(msg)
        else:
            raise error


@contextlib.contextmanager
def temp_particles_filename():
    """ Context manager provides temporary file

    Temporary file (and the directory it is in) will
    be destroyed after being used

    """
    temp_dir = tempfile.mkdtemp()
    yield os.path.join(temp_dir, "particles.xyz")
    shutil.rmtree(temp_dir)


# Attributes need to be either a float or integer
# so that they can be displayed in AViz.
_SUPPORTED_TYPES = [numpy.float64, numpy.int32]

# Used attribute info
_Info = namedtuple("_Info", ["key", "name", "shape", "used_length"])


# max number of properties that AViz supports
MAX_NUMBER_PROPERTIES = 8


def _determine_relevant_attributes(particles):
    """ Return an list of relevant cuba attributes on particles

    Returned list contains a list of attribute infos
    where the sum of the 'used_length' is less than or
    equal to MAX_NUMBER_PROPERTIES.  Additionally, all the attributes
    are either int or float as we can convert them to a float
    value for the Aviz file.

    """
    result = []
    used_keys = []
    number_properties = 0
    for particle in particles.iter_particles():
        data = particle.data
        for key in data:
            keyword = KEYWORDS[CUBA(key).name]
            if (key not in used_keys and
                    number_properties < 8 and
                    keyword.dtype in _SUPPORTED_TYPES):
                size_of_attribute = numpy.prod(keyword.shape)
                used_length = min(size_of_attribute,
                                  MAX_NUMBER_PROPERTIES - number_properties)
                number_properties += used_length

                result.append(_Info(key=key,
                                    name=keyword.name,
                                    shape=keyword.shape,
                                    used_length=used_length))
                used_keys.append(key)
        if number_properties is 8:
            break

    return result


def create_xyz_file(particles, filename):
    """ Convert particles dataset to an AViz file

    If particles have CUBA attributes, a maximum 8 of these
    attributes are written to the file and a description
    of these attributes is written to the end of the file.
    Such files can only be read by AViz version >=6.6.

    AViz properties are always of type float so only particle
    attributes of float or integer are supported.  Attributes
    of other types are ignored.

    Parameters
    ----------
    particles : ABCParticles
        The particles dataset to be written to file
    filename : str
        name of xyz file to be created

    """
    properties = _determine_relevant_attributes(particles)

    with open(filename, "w") as output_file:
        output_file.write(
            "{}\n".format(particles.count_of(CUDSItem.PARTICLE)))
        output_file.write("#XYZfile\n")
        for particle in particles.iter_particles():
            dummy_type = "X0"
            line = "{0} {1[0]:.16e} {1[1]:.16e} {1[2]:.16e}".format(
                    dummy_type,
                    particle.coordinates)

            # add each property
            data = particle.data
            for attribute_info in properties:
                if attribute_info.shape == [1]:
                    line += " {:.16e}".format(data[attribute_info.key])
                else:
                    for value in islice(data[attribute_info.key],
                                        attribute_info.used_length):
                        line += " {:.16e}".format(value)
            output_file.write(line + "\n")

        # write property information at end of file
        if properties:
            names = []
            for attribute_info in properties:
                names.extend([{"name": attribute_info.name}
                              for _ in xrange(attribute_info.used_length)])
            output_file.write(yaml.dump({'properties': names},
                                        default_flow_style=False))
