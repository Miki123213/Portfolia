from pylab import *
from scipy.interpolate import interp2d
from mpl_toolkits.mplot3d import Axes3D

p = 3

x = linspace(-p, p, 10)
y = linspace(-p, p, 10)

xx, yy = meshgrid(x, y)

rr = sqrt(xx**2 + yy**2)

zz = exp(-rr**2)

f1 = figure()
a1 = Axes3D(f1)

a1.scatter(xx, yy, zz, cmap="hot")

w = interp2d(x, y, zz, kind='linear')

x = linspace(-p, p, 50)
y = linspace(-p, p, 50)
xx, yy = meshgrid(x, y)

zz = w(x, y)
f2 = figure()
a2 = Axes3D(f2)

a2.plot_surface(xx, yy, zz, cmap="hot", rstride=1, cstride=1)

show()