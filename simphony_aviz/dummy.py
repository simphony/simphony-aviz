def show(dataset):
    """ Show a CUDS container

    Parameters
    ----------
    container : {ABCMesh, ABCParticles, ABCLattice}
        The CUDS container to be shown.

    Raises
    ------
    TypeError:
        If the container type is not supported by the engine.

    """
    raise NotImplementedError
