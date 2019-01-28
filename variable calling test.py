from vpython import *



a = sphere(pos=vector(0, 0, 0), radius=1, color=color.blue)
b = sphere(pos=vector(1, 1, 1), radius=1, color=color.red)

list(a,b)


def penguin():
    for i in range(0, 1):
        x = list(i).pos
        print(x)

penguin()