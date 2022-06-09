from pylab import *
def f(x):
    return sin(x) - x**2

a = 0.01
b = pi;
h = 1.0e-100

i = 0
while b-a > h:
    i += 1
    c = 0.5*(a + b)
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c


x0 = 0.5*(a+b)
x = linspace(0.01, pi, 100)
plot(x, f(x))
plot(x0, 0.0, ls="", marker="o")
grid()
print(i, x0 )
show()
