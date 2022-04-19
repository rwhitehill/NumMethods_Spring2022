#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
rcParams['text.usetex']         = True
rcParams['font.family']         = 'sans-serif'
rcParams['font.sans-serif']     = ['Helvetica']

def spline(dataX,dataY,t):
    a,b,c,d = spline_coeff(dataX,dataY)
    for i in range(len(dataX)-1):
        if dataX[i] <= t and dataX[i+1] >= t:
            break
    xk = dataX[i]
    y = a[i] + b[i]*(t-xk) + c[i]*(t-xk)**2.0 + d[i]*(t-xk)**3.0
    return y

def spline_coeff(dataX,dataY):
    n = len(dataX) - 1 
    h = np.zeros(n)
    for i in range(n):
        h[i] = dataX[i+1] - dataX[i] 
    A = np.zeros([n+1,n+1])
    A[0,0]   = 1.0
    A[-1,-1] = 1.0
    for i in range(1,n):
        A[i,i-1] = h[i-1]
        A[i,i+1] = h[i]
        A[i,i]   = 2.0*(h[i]+h[i-1])
    bb = np.zeros([n+1,1])
    for i in range(n):
        bb[i] = 3.0/h[i]*(dataY[i+1]-dataY[i]) - 3.0/h[i-1]*(dataY[i]-dataY[i-1])
    c = np.linalg.solve(A,bb)
    a = np.copy(dataY)
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(n):
        b[i] = 1.0/h[i]*(a[i+1]-a[i]) - h[i]/3.0*(2.0*c[i]+c[i+1])
        d[i] = (c[i+1]-c[i])/3.0/h[i]
    a = a[:-1]
    c = c[:-1]
    return a,b,c,d 

if __name__ == '__main__':
    
