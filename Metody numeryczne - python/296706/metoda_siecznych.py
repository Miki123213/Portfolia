from pylab import *

def f(x):
    return -x*(x-1)*(x-4)


x = [0.2, 2.5]
i = 1
h= 1.0e-10

while abs(x[i] - x[i-1]) > h:
    i+=1
    xi = x[i-1] - f(x[i-1])*(x[i-1] - x[i-2])/(f(x[i-1]) - f(x[i-2]))
    x.append(xi)

print i, xi, f(xi)

x = linspace(0, 3, 100)
plot(x, f(x))
plot(xi, 0.0, ls="", marker="o")
grid()
show()