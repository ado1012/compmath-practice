import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


xlist = np.linspace(-3, 3, 100)
ylist = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = (X-1)**2 + (8 * ((Y-1)**2))


def obj(x):
    x1 = x[0]
    x2 = x[1]
    f = (x1 - 1)**2 + 8*((x2-1)**2)
    g = np.array([2*(x1-1),16*(x2-1)])
    H = np.array([[2,0],[0,16]])
    return f,g,H

def steepest(obj,x):
    alpha = 0.05
    xv = np.array([x])
    while True:
        f,g,H = obj(x)
        s = -g
        x = x + alpha * s
        xv = np.vstack((xv,x))
        if norm(s) < 1.0E-6 :
            break
    return xv


def newton(obj,x):
    xv = np.array([x])
    while True:
        f,g,H = obj(x)
        s = -g
        x = x + np.linalg.inv(H).dot(s)
        xv = np.vstack((xv,x))
        if norm(s) < 1.0E-6 :
            break
    return xv


xinit = np.array([2,0])
res = steepest(obj, xinit)
res2 = newton(obj, xinit)
fig = plt.figure();plt.clf()
ax = fig.add_subplot(111)
levels = [1,2,5,10,15]

cp = plt.contour(X, Y, Z, levels)
ax.clabel(cp, inline=True,
          fontsize = 10)
ax.plot(1,1,"ob")
ax.plot(2,0,"or")
ax.plot(res[:,0], res[:,1],"ok")
ax.plot(res2[:,0],res2[:,1],"-")
ax.set_title('Contour Plot')
ax.set_xlabel("x (cm)")
ax.set_ylabel("y (cm)")
plt.show()
