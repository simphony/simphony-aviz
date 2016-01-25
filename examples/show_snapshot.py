
# from simphony.visualisation import aviz
from simphony.cuds.particles import Particles, Particle
from simphony_aviz.util import convert_particles_to_input_file
from simphony.core.cuba import CUBA

positions = [(1.0, 1.0, 1.0),
             (2.0, 2.0, 2.0),
             (1.5, 1.8, 1.9),
             (2.0, 1.0, 1.5)]
velocities = [(1.0, 1.0, 1.0),
              (2.0, 2.0, 2.0),
              (1.5, 1.8, 1.9),
              (2.0, 1.0, 1.5)]

mass = [1.0, 2.0, 10.0, 20]

# add particles
particles = [Particle(coordinates=positions[index],
                      data={CUBA.VELOCITY: velocities[index],
                            CUBA.MASS: mass[index]})
             for index, position in enumerate(positions)]

my_particles = Particles("test")
my_particles.add_particles(particles)

convert_particles_to_input_file(my_particles, "test.xyz")
# aviz.show(my_particles)
