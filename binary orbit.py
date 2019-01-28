from vpython import *

ballA = sphere(pos=vector(1.496*10**11,0,0),radius=6.371*10**6, color=color.blue)
ballB = sphere(pos=vector(0,0,0),radius=6.371*10**6, color=color.red)
ballC = sphere(pos=vector(0,0,0),radius=10, color=color.green)

BallAV = vector(0,460,0)
AMass = 5.972*10**24
BallBV = vector(0,-460,0)
BMass = 5.972*10**24

deltat = 5
G = 6.67408* 10**(-11)
for i in range(100000):
    rate(1000)
    ballA.pos += BallAV
    ballB.pos += BallBV
    dist = ((ballB.pos.x - ballA.pos.x) ** 2 + (ballB.pos.y - ballA.pos.y) ** 2 + (ballB.pos.z - ballA.pos.z) ** 2) ** 0.5
    Radialvector = vector(ballB.pos.x - ballA.pos.x, ballB.pos.y - ballA.pos.y, ballB.pos.z - ballA.pos.z)
    BallAV += ((deltat * G * BMass / (dist ** 3)) *Radialvector)
    BallBV += ((deltat * G * AMass / (dist ** 3)) *-Radialvector)


'''
F = MA
F = G M1 M2 / R**2
G M1 M2 / R**2 = M1A
G M2 / R**2 = A
V = U + AT
V = U + TGM2/R**3 * R
'''