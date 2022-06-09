# -*- coding: utf-8 -*-

from pylab import *
from scipy.interpolate import lagrange
from random import uniform
matplotlib.rc('font', family='Arial')

xm = -2
xx = 2
x = linspace(xm, xx, 100)
y = 4*x**4 +3*x**3 - 15*x**2 + x + 3
plot(x, y, label="pierwotna funkcja")

n = 19
r = []
for i in range(n):
    r.append(uniform(xm, xx))
r = sort(r)
y = 4*r**4 +3*r**3 - 15*r**2 + r + 3
plot(r, y, ls="", marker="o", markersize=10, label=u"losowe wartości funkcji")

w = lagrange(r, y)
print w
y = w(x)
plot(x, y, ls="--", lw=3, label=u"interpolacja Lagrange'a")

ylim(-40,40)
legend()
show()