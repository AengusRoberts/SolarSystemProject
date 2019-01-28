from vpython import *


class Planet:
    def __init__(self, x, y, z, mass, r):
        self.radius = r
        self.mass = mass
        self.pos = vector(x, y, z)

# ballA = sphere(pos=vector(5,0,0),radius=1, color=color.blue)

