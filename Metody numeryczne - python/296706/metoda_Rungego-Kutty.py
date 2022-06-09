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

def f(x,y):
    return -p(x) * y

def k1(x, y, i):
    return - dx * p(x[i]) * y[i]
    
def k2(x, y):
    return dx * f(x[i] + dx/2, y[i] + k1(x, y, i)/2)
    

y = [y0]
for i in range(len(x)-1):
    y.append(y[i] + k2(x,y))
    
subplot(121)
plot(x, r(x), label="analitycznie")
legend()

plot(x, y, label="numerycznie")
legend()

subplot(122)
plot(x, abs(y - r(x)), label=u"roznica", c="r")
legend()

show()
