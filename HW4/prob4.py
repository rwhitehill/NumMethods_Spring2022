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

def gen_plot(f,T,N,save_path,nodes='uniform'):
    F = f(T)
    
    ls = ['m-','y-','c-']
    fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(7*2,5))
    for n in N:
        if nodes == 'uniform': 
            x_data = np.linspace(-1.0,1.0,n+1)
        elif nodes == 'chebyshev':
            x_data = np.array([np.cos( (2*j+1)*np.pi / 2 / (n+1) ) for j in range(n+1)])
        y_data = f(x_data)
        
        interp = np.array([Lagrange_interp(t,x_data,y_data) for t in T])
        error  = F - interp
        ax[0].plot(T,interp,ls[N.index(n)],label=r'$n = %d$'%n)
        ax[1].plot(T,error,ls[N.index(n)])

    ax[0].plot(T,F,'k-.',label='$f(x)$')
    ax[1].axhline(y=0,color='k',linestyle='-.')
    ax[0].set_xlabel(r'$x$',size=20)
    ax[1].set_xlabel(r'$x$',size=20)
    ax[0].set_ylabel(r'$y$',size=20)
    ax[1].set_ylabel(r'$e(x)$',size=20)
    ax[0].tick_params(axis='both',which='major',labelsize=20,direction='in')
    ax[1].tick_params(axis='both',which='major',labelsize=20,direction='in')
    ax[0].legend(fontsize=20,frameon=False)
    plt.tight_layout()
    plt.savefig(save_path,bbox_inches='tight')

if __name__ == '__main__':
    
    f = lambda x: 1.0/(1.0 + 25.0*x**2.0)
    T = np.linspace(-1.0,1.0,100)
    N  = [5,10,20]

    gen_plot(f,T,N,'fig1.png',nodes='uniform')
    gen_plot(f,T,N,'fig2.png',nodes='chebyshev')
    
    uniform_nodes   = []
    chebyshev_nodes = []
    for n in N:
            uniform_nodes.append(np.linspace(-1.0,1.0,n+1))
            chebyshev_nodes.append(np.array([np.cos( (2*j+1)*np.pi / 2 / (n+1) ) for j in range(n+1)]))
    
    fix,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))
    for i in range(len(N)):
        y = -1*np.ones(N[i] + 1) + i
        y1 = y - 0.1
        y2 = y + 0.1

        ax.plot(uniform_nodes[i],y1,'k.')
        ax.plot(chebyshev_nodes[i],y2,'r.')
    ax.plot([],[],'r.',label='chebyshev')
    ax.plot([],[],'k.',label='uniform')
    for i in range(len(N)):
        ax.text(1.1,-1+i,r'$n=%d$'%N[i],fontsize=20)
    ax.set_xlim(right=1.5)
    ax.set_ylim(top=2.0)
    ax.set_xlabel(r'$x$',size=20)
    ax.tick_params(axis='both',which='major',labelsize=20,direction='in')
    ax.legend(loc='upper center',fontsize=15)
    plt.savefig('fig3.png',bbox_inches='tight')

    
