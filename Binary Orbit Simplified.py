from vpython import *

ballA = sphere(pos=vector(5, 0, 0), radius=1, color=color.blue)
ballA.trail = curve(color=ballA.color)
ballB = sphere(pos=vector(-5, 0, 0), radius=1, color=color.red)
ballB.trail = curve(color=ballB.color)
#ballC = sphere(pos=vector(0, 0, 0), radius=1, color=color.green)

BallAV = vector(0, 1, 0)
AMass = 60
BallBV = vector(1, -1, 0)
BMass = 30

deltat = 1
G = 1
for i in range(10000):
    rate(1)
    ballA.pos += BallAV
    ballB.pos += BallBV
    dist = ((ballB.pos.x - ballA.pos.x) ** 2 + (ballB.pos.y - ballA.pos.y) ** 2 + (
            ballB.pos.z - ballA.pos.z) ** 2) ** 0.5
    Radialvector = vector(ballB.pos.x - ballA.pos.x, ballB.pos.y - ballA.pos.y, ballB.pos.z - ballA.pos.z)
    BallAV += ((deltat * G * BMass / (dist ** 3)) * Radialvector)
    BallBV += ((deltat * G * AMass / (dist ** 3)) * -Radialvector)
    ballA.trail.append(pos=ballA.pos)
    ballB.trail.append(pos=ballB.pos)
    