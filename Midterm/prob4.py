#!/usr/bin/env python3

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
rcParams['text.usetex']         = True
rcParams['font.family']         = 'sans-serif'
rcParams['font.sans-serif']     = ['Helvetica']

x = sp.Symbol('x')
f = sp.exp(1-x**2)
f_num = sp.lambdify(x,f,'numpy')

X = np.linspace(-1,1,100)
fig, ax = plt.subplots(1,1,figsize=(7,5))
ax.plot(X,f_num(X),'k-',label='original')
for i in range(1,6):
    fi = f.series(x,0,i+1)
    fi = fi.removeO()
    print('T_{}(x) = {}'.format(i,fi))  
    fi_num = sp.lambdify(x,fi,'numpy')
    ax.plot(X,np.vectorize(fi_num)(X),label='order = %d'%i)

ax.set_xlabel(r'$x$',size=20)
ax.set_ylabel(r'$y$',size=20)
ax.tick_params(axis='both',which='major',labelsize=20,direction='in')
ax.legend(fontsize=15)
plt.savefig('./prob4.png',bbox_inches='tight')

