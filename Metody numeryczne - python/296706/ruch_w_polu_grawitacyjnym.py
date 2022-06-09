from pylab import *

R = 6.371e+6 # m
G = 6.674e-11
M = 5.972e+24 # kg

v0 = 30 # m/s


# 1

alp = radians(20.0)
dt = 0.001 #s

vx0 = v0 * cos(alp)
vy0 = v0 * sin(alp)

x0 = 0.0
y0 = R+10

x = [x0]
y = [y0]
vy = [vy0]
vx = [vx0]

i = 0
while y[i] - R >= 0.0:
    vx.append(vx[i] - 0.00*vx0)
    x.append(x[i] + dt*vx[i+1])
    vy.append(vy[i] - dt*G*M/y[i]**2)
    y.append(y[i] + vy[i+1]*dt)
    i += 1
    
print (i, i*dt, vy[i])

plot(x, array(y)-R)


grid()
show()
    