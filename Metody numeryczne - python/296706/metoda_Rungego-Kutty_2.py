# -*- coding: utf-8 -*-
from pylab import *

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
y = [y0]

for i in range(len(x)-1):
    k1 = dx * f(x[i], y[i])
    k2 = dx * f(x[i] + 0.5*dx, y[i] + 0.5*k1)
    y.append(y[i] + k2)
    
subplot(121)
plot(x, r(x), label="analitycznie")
legend()

plot(x, y, label="numerycznie")
legend()

subplot(122)
plot(x, abs(y - r(x)), label=u"roznica", c="r")
legend()

show()