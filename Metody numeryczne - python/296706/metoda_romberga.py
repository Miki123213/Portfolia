from scipy.integrate import romberg

a = -0.25
b = 1.25
def f(x):
    return 4*x**4 - 5*x**3 - 2*x**2 + x + 5

def C(x):
    return 4*x**5/5.0 - 5*x**4/4.0 - 2*x**3/3.0 +0.5*x**2 + 5*x

print "analitycznie I =", C(b) - C(a)

r = romberg(f, a, b, show=True)
print "m. Romberga I =", r