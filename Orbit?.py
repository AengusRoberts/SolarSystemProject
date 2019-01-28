from vpython import *
import math

sun = sphere(pos=vector(0, 0, 0), radius=100000, color=color.orange, mass=10000)
earth = sphere(pos=vector(1000000, 1000000, 1000000), radius=50000, color=color.blue, mass=1000)

earthv = vector(0, 0, 50000)
G = 6.67408 * (10 ** 11)


def fGrav(M1, M2, X1, X2, Y1, Y2, Z1, Z2):
    deltax = (X2 - X1)
    deltay = (Y2 - Y1)
    deltaz = (Z2 - Z1)
    r = ((deltax ** 2) + (deltay ** 2) + (deltaz ** 2)) ** 0.5
    fconstant = (G * M1 * M2) / r ** 3
    f = vectorMultiplier(deltax, deltay, deltaz, fconstant)
    return (f)


def dist(X1, Y1, Z1, X2, Y2, Z2):
    deltax = (X2 - X1)
    deltay = (Y2 - Y1)
    deltaz = (Z2 - Z1)
    r = ((deltax ** 2) + (deltay ** 2) + (deltaz ** 2)) ** 0.5
    return (r)


def delta(A, B):
    return (((B - A) ** 2) ** 0.5)


def vectorMultiplier(A, B, C, D):
    x = [A, B, C]
    y = [i * D for i in x]
    return tuple(y)


def vFromGrav(M, R, X1, Y1, Z1, X2, Y2, Z2):
    xvelocity = math.sqrt(((G * M) / (R ** 2)) * delta(X1, X2))
    yvelocity = math.sqrt(((G * M) / (R ** 2)) * delta(Y1, Y2))
    zvelocity = math, sqrt(((G * M) / (R ** 2)) * delta(Z1, Z2))
    a = (xvelocity, yvelocity, zvelocity)
    return (a)


for i in range(1000):
    rate(100)
    earth.pos = earth.pos + earthv
    x = vFromGrav(sun.mass, dist(sun.pos.x, sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z), sun.pos.x,
                  sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z)[0]
    y = vFromGrav(sun.mass, dist(sun.pos.x, sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z), sun.pos.x,
                  sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z)[1]
    z = vFromGrav(sun.mass, dist(sun.pos.x, sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z), sun.pos.x,
                  sun.pos.y, sun.pos.z, earth.pos.x, earth.pos.y, earth.pos.z)[2]
    earthv = earthv + vector(x, y, z)
print(fGrav(sun.mass, earth.mass, sun.pos.x, earth.pos.x, sun.pos.y, earth.pos.y, sun.pos.z, earth.pos.z))
