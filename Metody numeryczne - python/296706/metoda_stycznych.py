from pylab import *

def f(x):
    return x**2 - x

def d(x):
    return 2*x - 1
    
h = 1.0e-9
#a = 0
#b = 2

x = [1.5]
i = 0

while True:
    x.append(x[i] - f(x[i])/d(x[i]))
    if abs(x[i+1] - x[i]) < h: break
    print i, x[i]
    i += 1
        
print x[i], f(x[i+1])
        