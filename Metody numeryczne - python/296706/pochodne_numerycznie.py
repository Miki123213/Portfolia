from pylab import *
def f(x):
    return x**3 - 3*x**2 + 2*x + 3

def pa(x):
    return 3*x**2 - 6*x + 2

h = 0.1
x = linspace(-1, 3, 100)

y = f(x)

ya = pa(x)


def pnp(x):
    return (f(x + h) - f(x))/h
yp = pnp(x)


def pnt(x):
    return (f(x) - f(x - h))/h
yt = pnt(x)

def pnc(x):
    return (f(x + h) - f(x - h))/(2*h)
yc = pnc(x)

plot(x, y)
plot(x, ya)
plot(x, yp)
plot(x, yt)
plot(x, yc)
show()

