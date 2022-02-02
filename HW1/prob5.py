#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
rcParams['text.usetex']         = True
rcParams['font.family']         = 'sans-serif'
rcParams['font.sans-serif']     = ['Helvetica']

x = np.linspace(0,1)
f1 = np.exp(x)
f2 = 1 + x + x**2/np.math.factorial(2)

fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))
ax.plot(x,f1,'k-',label=r'$f_1(x) = e^x$')
ax.plot(x,f2,'b.',label=r'$f_2(x) = 1+x+\frac{x^2}{2!}$')
ax.legend(loc=2,fontsize=20)

ax.set_xlabel(r'$x$',size=20)
ax.set_ylabel(r'$f(x)$',size=20)
ax.tick_params(axis='both',which='major',labelsize=20,direction='in')

plt.savefig('prob5fig.png',bbox_inches='tight')
