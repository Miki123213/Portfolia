from scipy.interpolate import interp1d
from scipy.integrate import trapz
from pylab import *

x = [0.0, 1.0, 1.5, 2.0, 3.0]
y = [1.0, 3.0, 2.125, 1.0, 1.0]
plot(x, y,ls="", marker="o", markersize=10)

xx = linspace(0, 3, 100)

w1 = interp1d(x, y, kind="quadratic")
yy = w1(xx)
plot(xx, yy)
print(trapz(yy, xx))

w2 = interp1d(x, y, kind="cubic")
yy = w2(xx)
plot(xx, yy)
print(trapz(yy, xx))


show()