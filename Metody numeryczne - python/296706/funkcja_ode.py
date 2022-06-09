# -*- coding: utf-8 -*-
from pylab import *
from scipy.integrate import ode

x0 = 1
y0 = 2
x = linspace(1, 10, 100)
dx = x[1] - x[0]


def p(x):
    return -(2*x - 1)/(x**2)
    
def P(x):
    return -(log(x**2) + 1/x)

def r(x):
    return y0 * exp(P(x0) - P(x))

def f(x, y):
    return -p(x)*y
    

row = ode(f)
row.set_integrator('dopri5')
row.set_initial_value(y0, x0)

xn = 10.0

y = [y0]
while row.successful() and (row.t+dx) < xn:
    q = float(row.integrate(row.t+dx))
    y.append(q)
    

y1 = [y0]
for i in range(len(x)-1):
    k1 = dx * f(x[i], y1[i])
    k2 = dx * f(x[i] + 0.5*dx, y1[i] + 0.5*k1)
    y1.append(y1[i] + k2)


y2 = [y0]

for i in range(len(x)-1):
    k1 = dx * f(x[i], y2[i])
    k2 = dx * f(x[i] + 0.5*dx, y2[i] + 0.5*k1)
    k3 = dx * f(x[i] + 0.5*dx, y2[i] + 0.5*k2)
    k4 = dx * f(x[i] + dx, y2[i] + k3)
    y2.append(y2[i] + (k1 + 2*k2 + 2*k3 + k4)/6.0)


    
subplot(221)
plot(x, r(x), label="analitycznie")
legend()

plot(x, y1, label="2 rzedu")
legend()
plot(x, y2, label="4 rzedu")
legend()

plot(x, y, label="dopri5")
legend()


subplot(222)
plot(x, abs(y1 - r(x)), label=u"roznica 2 rzedu", c="r")
legend()

subplot(223)
plot(x, abs(y2 - r(x)), label=u"roznica 4 rzedu", c="r")
legend()

subplot(224)
plot(x, abs(y - r(x)), label=u"roznica dopri5", c="r")
legend()

show()