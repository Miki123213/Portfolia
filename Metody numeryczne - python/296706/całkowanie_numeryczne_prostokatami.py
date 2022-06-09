def f(x):
    #return 4*x**4 - 5*x**3 - 2*x**2 + x + 5
    return 1.0/x
def F(x):
    return 4*x**5/5.0 - 5*x**4/4.0 - 2*x**3/3.0 +0.5*x**2 + 5*x

#a = -0.25
#b = 1.25
a = 0.01
b = 100
n = 100000

def cnp(f, a, b, n):
    dx = (b-a)/n
    xi = a + 0.5*dx
    sm = 0
    for i in range(n):
        sm += f(xi)
        xi += dx
    return sm * dx
    
def cnt(f, a, b, n):
    dx = (b-a)/n
    xi = a + dx
    sm = 0.5*f(a) + 0.5*f(b)
    for i in range(n-1):
        sm += f(xi)
        xi += dx
    return dx * sm
    
IP = cnp(f, a, b, n)
IT = cnt(f, a, b, n)
IA = F(b) - F(a)

print ("IP =", IP)
print ("IT =", IT)
print ("IA =", IA)
ET = abs(IA - IT)
EP = abs(IA - IP)
print (ET/EP)