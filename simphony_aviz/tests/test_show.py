import unittest
import random
import multiprocessing
import os

from simphony_aviz.show import show
from simphony.cuds.lattice import make_square_lattice
from simphony.cuds.mesh import Mesh
from simphony.cuds.particles import Particles, Particle


class TestShow(unittest.TestCase):
    def test_particles_show(self):
        def run_show():
            particles = Particles("test")
            random.seed(42)
            for i in range(0, 1000):
                p = Particle(coordinates=(random.uniform(0.0, 10.0),
                                          random.uniform(0.0, 10.0),
                                          random.uniform(0.0, 10.0)))
                particles.add_particles([p])

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
        os.system("killall -y 5s aviz")

    def test_lattice_show(self):
        lattice = make_square_lattice(
            'test', 0.2, (10, 10), origin=(0.2, -2.4))

        def function():
            with self.assertRaises(ValueError):
                show(lattice)

    def test_mesh_show(self):
        mesh = Mesh('test')

        def function():
            with self.assertRaises(ValueError):
                show(mesh)

    def test_unknown_container(self):
        container = object()
        with self.assertRaises(TypeError):
            show(container)
