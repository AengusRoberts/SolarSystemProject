import math

def vFromGrav(M,R,X1,Y1,Z1,X2,Y2,Z2):
    xvelocity = math.sqrt(((G*M)/(R**2))*delta(X1,X2))
    yvelocity = math.sqrt(((G*M)/(R**2))*delta(Y1,Y2))
    zvelocity = math.sqrt(((G*M)/(R**2))*delta(Z1,Z2))
    a = (xvelocity,yvelocity,zvelocity)
    return (a)

def delta(A,B):
    return (((B-A)**2)**0.5)

G = 7
print (vFromGrav(1,2,3,4,5,6,7,9)[1])