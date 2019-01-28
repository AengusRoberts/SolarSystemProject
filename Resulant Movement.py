from vpython import *
ball = sphere(pos=vector(2,2,2),radius = 5, color = color.yellow)
box = box(pos=vector(0,0,0),size = vector(1,1,1),color = color.red)

ballV = vector(0,0,0)
ForceA = vector(0,0,1)
ForceB = vector(0,0,1)
BallMass = 2

deltat = 0.05
t = 1
while t < 2:
    rate(10)
    ball.pos = ball.pos + ballV
    velocity = ((ForceA + ForceB)/BallMass)*deltat
    ballV = ballV + velocity
    print(ballV)