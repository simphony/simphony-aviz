import unittest
import random

from pyface.ui.qt4.util.gui_test_assistant import GuiTestAssistant
from pyface.ui.qt4.util.modal_dialog_tester import ModalDialogTester

from simphony_aviz.show import show
from simphony.cuds.lattice import make_square_lattice
from simphony.cuds.mesh import Mesh
from simphony.cuds.particles import Particles, Particle


class TestShow(GuiTestAssistant, unittest.TestCase):
    def setUp(self):
        GuiTestAssistant.setUp(self)

    def tearDown(self):
        GuiTestAssistant.tearDown(self)

    def test_particles_show(self):
        particles = Particles("test")
        random.seed(42)
        for i in range(0, 1000):
            p = Particle(coordinates=(random.uniform(0.0, 10.0),
                                      random.uniform(0.0, 10.0),
                                      random.uniform(0.0, 10.0)))
            particles.add_particles([p])

        def function():
            show(particles)
        return True

        tester = ModalDialogTester(function)
        tester.open_and_run(when_opened=lambda x: x.close(accept=False))
        self.assertTrue(tester.result)

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
