# -*- coding: utf-8 -*-

from pylab import *
from scipy.interpolate import lagrange
from random import uniform
matplotlib.rc('font', family='Arial')

xm = -pi
xx = pi
x = linspace(xm, xx, 100)
y = sin(x)
plot(x, y, label="pierwotna funkcja")

n = 10
r = []
for i in range(n):
    r.append(uniform(xm, xx))
r = sort(r)
y = sin(r)
plot(r, y, ls="", marker="o", markersize=10, label=u"losowe wartości funkcji")

w = lagrange(r, y)
print w
y = w(x)
plot(x, y, ls="--", lw=3, label=u"interpolacja Lagrange'a")

ylim(-1.5,1.5)
legend()
show()