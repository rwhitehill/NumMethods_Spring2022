#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
rcParams['text.usetex']         = True
rcParams['font.family']         = 'sans-serif'
rcParams['font.sans-serif']     = ['Helvetica']

def Lagrange_poly(t,x,i):
    res = 1.0
    for j in range(len(x)):
        if j == i:
            continue
        else:
            res *= (t-x[j])/(x[i]-x[j])
    return res

def Lagrange_interp(t,x,y):
    res = 0.0
    for i in range(len(x)):
        res += y[i]*Lagrange_poly(t,x,i)
    return res

if __name__ == '__main__':
    
    f = lambda x: 1.0/(1.0 + x**2.0)
    T = np.linspace(-1.0,1.0)

    fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))
    for n in range(1,11):
        x_data = np.linspace(-1.0,1.0,n+1)
        y_data = f(x_data)
        
        interp = np.array([Lagrange_interp(t,x_data,y_data) for t in T])
        ax.plot(T,interp)

    ax.plot(T,f(T),'k-X')
    ax.set_xlabel(r'$x$',size=20)
    ax.set_ylabel(r'$y$',size=20)
    ax.tick_params(axis='both',which='major',labelsize=20,direction='in')
    plt.savefig('fig1.png',bbox_inches='tight')

    
