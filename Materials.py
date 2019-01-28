from vpython import *

planets = (Earth, Mars, Jupiter, Saturn, Venus)

Earth = sphere(pos=vector(10, 0, 0), radius=1, color=color.blue, velocity=vector(0, 1, 0), mass=5.97 * 10 ** 24)
Mars = sphere(pos=vector(12, 0, 0), radius=0.6, color=color.red, velocity=vector(0, 1, 0), )
Jupiter = sphere(pos=vector(20, 0, 0), radius=4, color=color.orange, velocity=vector(0, 2, 0))
Saturn = sphere(pos=vector(28, 0, 0), radius=3.5, color=color.yellow, velocity=vector(0, 2, 0))
Venus = sphere(pos=vector(3.5, 0, 0), radius=.9, color=color.magenta, velocity=vector(0, 1, 0))
Sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.gray, velocity=0, mass=)

deltat = 1
g = 6.67 * 10 ** (-11)


def distCalc(x1, y1, z1, x2, y2, z2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2) ** 0.5)


def planetIteration():
    for i in range(0, len(planets)):
        planets(i)


def forceCalc():
    for i in range(0, len(planets)):
