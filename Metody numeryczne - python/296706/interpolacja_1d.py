from scipy.interpolate import interp1d
from pylab import *
from random import uniform

xm = -2
xx = 2
x = linspace(xm, xx, 100)

def f(x):
    return -3*x**3 + 2*x**2 + 5*x - 7
    
y = f(x)
plot(x, y)

r = array([uniform(xm, xx) for i in range(50)])
r = sort(r)
z = f(r)
plot(r, z, ls="", marker="o", markersize=10)

w = interp1d(r, z, kind="cubic")
x = linspace(min(r), max(r), 1000)
plot(x, w(x))


show()
      