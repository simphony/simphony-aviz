import unittest
import random
import multiprocessing
import os

from simphony.cuds.mesh import Mesh
from simphony.cuds.particles import Particles, Particle

from simphony_aviz.show import show
from simphony_aviz.testing.utils import create_lattice


class TestShow(unittest.TestCase):
    def test_particles_show(self):
        def run_show():
            particles = Particles("test")
            random.seed(42)
            for i in range(0, 1000):
                particle = Particle(coordinates=(random.uniform(0.0, 10.0),
                                                 random.uniform(0.0, 10.0),
                                                 random.uniform(0.0, 10.0)))
                particles.add([particle])

            show(particles)

        p = multiprocessing.Process(target=run_show)
        p.daemon = True
        p.start()
        p.join(timeout=2)
        self.assertTrue(p.is_alive())
        p.terminate()
        p.join()
        # TODO: Killing aviz manually
        # as descendant Aviz processes
        # could not be terminated.
        os.system("killall -y 3s aviz")

    def test_lattice_show(self):
        lattice = create_lattice()

        with self.assertRaises(TypeError):
            show(lattice)

    def test_mesh_show(self):
        mesh = Mesh('test')

        with self.assertRaises(TypeError):
            show(mesh)

    def test_unknown_container(self):
        container = object()
        with self.assertRaises(TypeError):
            show(container)


if __name__ == '__main__':
    unittest.main()
