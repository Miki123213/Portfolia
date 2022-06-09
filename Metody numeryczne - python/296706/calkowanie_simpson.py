from scipy.integrate import trapz, simps, newton_cotes
from numpy import linspace, sin, cos, pi

a = -0.25
b = 1.25
n = 10
w, e = newton_cotes(n, equal=True)

def f(x):
    return 4*x**4 - 5*x**3 - 2*x**2 + x + 5

def C(x):
    return 4*x**5/5.0 - 5*x**4/4.0 - 2*x**3/3.0 +0.5*x**2 + 5*x

I = C(b) - C(a)
x = linspace(a, b, n+1)
y = f(x)
T = trapz(y, x)
S = simps(y, x)

def NC(x):
    dx = x[1] - x[0]
    sm = 0
    for i in range(n+1):
        sm += w[i]*f(x[i])
    return sm * dx

N = NC(x)
print(w)
print ("I =", I, "T =", T, "S =", S, "N =", N)