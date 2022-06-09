from scipy.integrate import romberg, trapz, quad
from numpy import logspace, log10

def f(x):
    return x**(-2)

a = 1.0
b = 1000.0
n = 1000

x = logspace(log10(a), log10(b), n+1)
y = f(x)

print "trapz() =", trapz(y, x)
print "quad() =", quad(f, a, b, full_output=True)
print "romberg() =", romberg(f, a, b, show=True, divmax = 15) 

