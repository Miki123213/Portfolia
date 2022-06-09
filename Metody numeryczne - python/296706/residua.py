from pylab import *
def f(x):
    return exp(-x/10)*sin(x)

def pa(x):
    return exp(-0.1*x)*(cos(x) - 0.1*sin(x))

h = 0.1
x = linspace(0, 10*pi, 100)

y = f(x)

ya = pa(x)

yp = (f(x + h) - f(x))/h

yt = (f(x) - f(x - h))/h

yc = (f(x + h) - f(x - h))/(2*h)

#plot(x, y)
#plot(x, ya)
plot(x, yp - ya)
plot(x, yt - ya)
plot(x, yc - ya)
show()