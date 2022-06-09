from numpy import logspace, log10
from scipy.integrate import trapz

a = 0.01
b = 100

def f(x):
    return 1.0/x
    
n = 1000
x = logspace(log10(a), log10(b), n+1)
y = f(x)
T = trapz(y, x)
print ("trapz() =", T)