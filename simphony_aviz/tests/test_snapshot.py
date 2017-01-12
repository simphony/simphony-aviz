import unittest
import random
import os
import shutil
import tempfile

from PIL import Image

from simphony.cuds.mesh import Mesh
from simphony.cuds.particles import Particles, Particle

from simphony_aviz.snapshot import snapshot
from simphony_aviz.testing.utils import create_lattice


class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(self.temp_dir, 'test.png')
        self.addCleanup(self.cleanup)

    def cleanup(self):
        shutil.rmtree(self.temp_dir)

    def test_particles_snapshot(self):
        particles = Particles("test")
        random.seed(42)
        for i in range(0, 1000):
            p = Particle(coordinates=(random.uniform(0.0, 10.0),
                                      random.uniform(0.0, 10.0),
                                      random.uniform(0.0, 10.0)))
            particles.add([p])

        snapshot(particles, self.filename)
        self.assertTrue(os.path.exists(self.filename))
        image = Image.open(self.filename)
        self.assertTrue(image.size)
        self.assertTrue(image.size[0] > 0 and image.size[1] > 0)

    def test_lattice_snapshot(self):
        lattice = create_lattice()

        with self.assertRaises(TypeError):
            snapshot(lattice, "fail.png")

    def test_mesh_snapshot(self):
        mesh = Mesh('test')

        with self.assertRaises(TypeError):
            snapshot(mesh, "fail.png")

    def test_unknown_container(self):
        container = object()
        with self.assertRaises(TypeError):
            snapshot(container, "fail.png")


if __name__ == '__main__':
    unittest.main()
