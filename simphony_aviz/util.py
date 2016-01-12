import contextlib
import errno
import os
import shutil
import subprocess
import tempfile

from simphony.core.cuds_item import CUDSItem


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


def convert_particles_to_input_file(particles, filename):
    """ Convert particles dataset to an AViz file

    """
    with open(filename, "w") as output_file:
        output_file.write(
            "{}\n".format(particles.count_of(CUDSItem.PARTICLE)))
        output_file.write("#XYZfile\n")
        for particle in particles.iter_particles():
            dummy_type = "X0"
            output_file.write(
                "{0} {1[0]:.16e} {1[1]:.16e} {1[2]:.16e}\n".format(
                    dummy_type,
                    particle.coordinates))
