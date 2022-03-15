import matplotlib.pyplot as plt
import numpy as np
import math as m

def frange(a,b,d):
    ran = []
    c = m.ceil((b-a)/d)
    for i in range(0,c):
        ran.append(a+i*d)
    return ran

def plotf(f):
    y = f
    plt.plot(x,y,'ro')
    plt.show
    plt.savefig('sinx.png')


x = frange(1,14,2)
plotf(np.sin(x))