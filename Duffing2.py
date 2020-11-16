import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate
from matplotlib import pyplot as plt
from matplotlib import cm
import time
import os
import matplotlib.animation as animation

alpha = -1      # -1
beta = 1         # 1
delta = 0.3       # 0.3
gam = 0.15    # 0.15
w = 1
def flow_deriv(x_y_z,tspan):
    x, y, z = x_y_z
    a = y
    b = delta*np.cos(w*tspan) - alpha*x - beta*x**3 - gam*y
    c = w
    return[a,b,c]

def duffing(alpha,beta,gam,delta,w):
    # plt.close('all')
    T = 2*np.pi/w
    px1 = np.random.rand(1)
    xp1 = np.random.rand(1)
    w1 = 0

    x_y_z = [xp1, px1, w1]

    # Settle-down Solve for the trajectories
    t = np.linspace(0, 2000, 40000)
    x_t = integrate.odeint(flow_deriv, x_y_z, t)
    x0 = x_t[39999,0:3]

    tspan = np.linspace(1,20000,400000)
    x_t = integrate.odeint(flow_deriv, x0, tspan)
    siztmp = np.shape(x_t)
    siz = siztmp[0]

    y1 = x_t[:,0]
    y2 = x_t[:,1]
    y3 = x_t[:,2]

    plt.figure(2)
    lines = plt.plot(y1[1:2000],y2[1:2000],'ko',ms=1)
    plt.setp(lines, linewidth=0.5)
    plt.xlabel("x label ")
    plt.ylabel("y label ")
    plt.savefig('static/lines.png')
    fig = plt.figure()
    ims = []
    l = 6
    for cloop in range(0,l):
        phase = np.pi*cloop/l
        repnum = 5000
        px = np.zeros(shape=(2*repnum,))
        xvar = np.zeros(shape=(2*repnum,))
        cnt = -1
        testwt = np.mod(tspan-phase,T)-0.5*T;
        last = testwt[1]
        for loop in range(2,siz):
            if (last < 0)and(testwt[loop] > 0):
                cnt = cnt+1
                del1 = -testwt[loop-1]/(testwt[loop] - testwt[loop-1])
                px[cnt] = (y2[loop]-y2[loop-1])*del1 + y2[loop-1]
                xvar[cnt] = (y1[loop]-y1[loop-1])*del1 + y1[loop-1]
                last = testwt[loop]
            else:
                last = testwt[loop]
        plt.xlabel("x label ")
        plt.ylabel("y label ")
        lines = plt.plot(xvar,px,'bo',ms=1)
        ims.append(lines)

    ani = animation.ArtistAnimation(fig, ims, interval=120, blit=True,
                                    repeat_delay=1000)
    ani.save('static/dynamic_images.gif', writer='imagemagick')

