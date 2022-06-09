from pylab import *
from scipy.misc import derivative

h = 0.1
x = linspace(0, 2*pi, 1000)

def f(x):
    return sin(x**2)

def f2(x):
    return 2*cos(x**2) - sin(x**2)*4*x**2


yp = (f(x + h) - 2*f(x) + f(x - h))/(h**2)

d = derivative(f, x, n=2, dx = 0.1, order = 5)

plot(x, f(x))
plot(x, yp)
plot(x, d)
show()
