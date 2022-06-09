from pylab import *
 
prc = 100
 
AU  = 149597890.0e+3  # odleglosc Ziemia Slonce
G   = 6.67428e-11     # stala grawitacji [m^3 / (kg*s^2)]
RS  = 365*24*3600.0   # rok [s]
MS  = 1.98910e+30     # masa Slonca [kg]
VZ  = 29.78e+3        # predkosc Ziemi [m/s]
 
rx = AU
ry = 0.0
rc = sqrt(rx*rx + ry*ry)
 
ac = G * MS / (rc*rc)
ax = -ac*rx/rc
ay = -ac*ry/rc
 
vx = 0.0
vy = -VZ
 
tc = 0.0
dt = RS / (prc - 1.0)
 
figure(figsize=(8, 8), dpi=100)
 
plot(0, 0, ls="", marker="o", c="yellow", markersize=15)

xlim(-1.5, 1.5)
ylim(-1.5, 1.5)

text(0.1, -0.02, u"Slonce")
text(1.1, -0.02, "Ziemia")
xlabel("$r_x$ [AU]")
ylabel("$r_y$ [AU]")
title("orbita")
grid()
ion()
show()

for n in range(prc):
    print ("krok: %03d, czas: %5.2f" % (n, tc/RS))
    
    rx = rx + dt*vx
    ry = ry + dt*vy
    rc = sqrt(rx*rx + ry*ry)
    
    plot(rx/AU, ry/AU, ls="", marker="o", color="blue")
    draw()
    
    ac = G * MS / (rc*rc)
    ax = -ac*rx/rc
    ay = -ac*ry/rc
    
    vx = vx + ax*dt
    vy = vy + ay*dt
    
    tc += dt
    

    
raw_input()
 
 


