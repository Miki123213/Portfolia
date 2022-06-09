from pylab import *

x = linspace(0, 2*pi, 1000)
h1 = 1e-5
h2 = 1e-6
h3 = 1e-7
def f(x):
    return sin(x)*cos(10*x)

def pa(x):
    return cos(x)*cos(10*x) - 10*sin(x)*sin(10*x)

ya = pa(x)

yc1 = (f(x + h1) - f(x - h1))/(2*h1)
yc2 = (f(x + h2) - f(x - h2))/(2*h2)
yc3 = (f(x + h3) - f(x - h3))/(2*h3)

plot(x, yc1 - ya)
plot(x, yc2 - ya)
plot(x, yc3 - ya)
show()