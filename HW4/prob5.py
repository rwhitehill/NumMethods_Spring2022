#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
rcParams['text.usetex']         = True
rcParams['font.family']         = 'sans-serif'
rcParams['font.sans-serif']     = ['Helvetica']

import csv
from scipy.interpolate import interp1d

def spline(dataX,dataY,t):
    a,b,c,d = spline_coeff(dataX,dataY)
    for i in range(len(dataX)-1):
        if dataX[i] <= t and dataX[i+1] >= t:
            k = i
            break
    xk = dataX[k]
    y = a[k] + b[k]*(t-xk) + c[k]*(t-xk)**2.0 + d[k]*(t-xk)**3.0
    return y

def spline_coeff(dataX,dataY,printA=False):
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
    bb = np.zeros(n+1)
    for i in range(1,n):
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

    file = open('prob5.txt') 

    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)

    x_data = []
    y_data = []
    for row in csvreader:
        x_data.append(float(row[0]))
        y_data.append(float(row[1]))
    file.close()
    
    x_data = np.array(x_data)
    y_data = -1.0 * np.array(y_data)

    T = np.linspace(min(x_data),max(x_data),100)
    reconstruct = np.array([spline(x_data,y_data,t) for t in T])
    f = interp1d(x_data,y_data,kind='cubic')

    a,b,c,d = spline_coeff(x_data,y_data,True)
    #for i in range(len(a)):
    #    print('%.5f  %.5f  %.5f  %.5f'%(a[i],b[i],c[i],d[i]))

    fig,ax = plt.subplots(nrows=1,ncols=1,figsize=(7,5))
    ax.plot(T,reconstruct,'c')
    ax.plot(x_data,y_data,'k*')
    ax.tick_params(axis='both',which='major',labelsize=20,direction='in')
    plt.savefig('./fig4.png',bbox_inches='tight')
    
