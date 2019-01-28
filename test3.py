from vpython import *

Sun = sphere(pos=vector(0,0,0), radius = 100, color = color.orange)
earth = sphere(pos=vector(-200,0,0), radius = 10, color = color.blue, make_trail = True)

earthv = vector(0,1,60)
sunv = vector(0,0,0)

vscale = 10
varr = arrow(pos=earth.pos, axis=vscale * earthv, color=color.yellow)

for i in range(1000):
    rate(100)
    earth.pos = earth.pos +earthv
    dist = (earth.pos.x**2 + earth.pos.y**2 + earth.pos.z**2)**0.5
    RadialVector = (earth.pos - Sun.pos)/dist
    Fgrav = -10000*RadialVector/dist**2
    earthv = earthv + Fgrav
    earth.pos += earthv
    if dist <= Sun.radius: break
    varr.pos = varr.pos + earthv
    varr.axis =  Fgrav * vscale


