# -*- coding: utf-8 -*-
from scipy.integrate import fixed_quad, quadrature, quad
from math import log

a = 0.1
b = 1000.0

def f(x):
    return 1/x

def C(x):
    return log(x)

print u"dokładny wynik", C(b) - C(a)
print "fixed_quad(.., n=10)", fixed_quad(f, a, b, n=10)
print "quadrature()", quadrature(f, a, b, tol=1.0e-6)
print "quad()", quad(f, a, b)