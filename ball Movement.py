from vpython import *


def newton2(FX, FY, FZ, M):
    x = [FX, FY, FZ]
    A = [i / M for i in x]
    return A

def vecScale(A,B,C,D):
    x = [A,B,C]
    A = [i * D for i in x]
    return tuple(A)

ball = sphere(pos=vector(0, 0, 0), radius=10, color=color.blue)
ball.velocity = vector(0, 0, 0)
t = 1
deltat = 0.01
box = box(pos=vector(-1, -1, -1), size=vector(10, 10, 10), color=color.red)
while t < 2:
    rate(100)
    ball.pos = ball.pos + ball.velocity * deltat
    NewX = newton2(1,1,1,1)[0]
    NewY = newton2(1,1,1,1)[1]
    NewZ = newton2(1,1,1,1)[2]
    VelVec = vecScale(NewX,NewY,NewZ,t)
    ball.velocity += vector(VelVec[0],VelVec[1],VelVec[2])
    t += deltat