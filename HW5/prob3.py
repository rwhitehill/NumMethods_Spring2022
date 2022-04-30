#!/usr/bin/env python

import numpy as np
import pandas as pd

def deriv(f,a,h):
    faph = f(a+h)
    fa   = f(a)
    famh = f(a-h)
    forward  = (faph - fa) / h
    backward = (fa - famh) / h
    return np.array([forward,backward])

def order(errors):
    orders = []
    for i in range(1,len(errors)):
        orders.append(np.log2(errors[i-1]/errors[i]))
    return orders 

if __name__ == '__main__':

    f  = np.sin
    fp = np.cos
    h = np.array([0.1,0.05,0.025,0.0125,0.00625])

    results = {}

    for A in [0.5,0.6,0.7]:
        derivs = np.array([deriv(f,A,H) for H in h])
        exact  = fp(A)
        errors = abs(exact - derivs)
        forward_order  = order(errors[:,0])
        backward_order = order(errors[:,1])
        
        results = {}

        results['$h$'] = ['0.1','0.05','0.025','0.0125','0.00625']

        results[r'\makecell{Forward \\ Difference}'] = ['%.5f'%_ for _ in derivs[:,0]]
        results[r'\makecell{Forward \\ Error}']  = ['%.5f'%_ for _ in errors[:,0]]
        results[r'\makecell{Forward \\ Order}']  = ['-'] + ['%.5f'%_ for _ in order(errors[:,0])]

        results[r'\makecell{Backward \\ Difference}'] = ['%.5f'%_ for _ in derivs[:,1]]
        results[r'\makecell{Backward \\ Error}'] = ['%.5f'%_ for _ in errors[:,1]]
        results[r'\makecell{Backward \\ Order}']= ['-'] + ['%.5f'%_ for _ in  order(errors[:,1])] 
        
        table = pd.DataFrame(results)

        A_str = str(A).replace('.','-')
        table.to_latex(buf='prob3_%s.tex'%A_str,
                index=False,
                escape=False,
                column_format='lcccccc',
                caption='Table for $a = %.1f$, where $f\'(%.1f) = %.5f$'%(A,A,fp(A)))      




