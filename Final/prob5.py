#!/usr/bin/env python3

import numpy as np
import pandas as pd

def trap_int(f,a,b,n):
    h = (b-a)/float(n)
    X = np.linspace(a,b,n+1)
    Y = f(X)
    
    result = 0.0
    for i in range(n):
        result += h/2.0 * (Y[i] + Y[i+1])
    return result #h/2.0 * (Y[0] + 2*np.sum(Y[1:-1]) + Y[-1])

def simp_int(f,a,b,n):
    h = (b-a)/float(n)
    X = np.linspace(a,b,n+1)
    Y = f(X)
    
    result = 0.0
    for i in range(int(n/2)):
        l = 2*i
        result += h/3.0 * (Y[l] + 4.0*Y[l+1] + Y[l+2]) 
    return result

def ratio(errors):
    num = errors[:-1]
    den = errors[1:]
    return num/den 

def order(ratios):
    return np.log2(ratios)

def get_results(approx):
    errors = abs(1.0 - approx)
    ratios = ratio(errors)
    orders = order(ratios)
    return errors,ratios,orders

if __name__ == '__main__':

    f = np.sin
    a = 0.0;b=np.pi/2.0
    exact = 1.0 

    results = {}
    results[r'$n$'] = ['%d'%2**i for i in range(6)]

    N = [1,2,4,8,16,32]
    trap = np.array([trap_int(f,a,b,_) for _ in N])
    simp = np.array([simp_int(f,a,b,_) for _ in N[1:]])

    trap_res = get_results(trap)
    simp_res = get_results(simp)
    
    results[r'$T_n(f)$']   = ['%.5f'%_ for _ in trap]
    results[r'T error(n)'] = ['%.5f'%_ for _ in trap_res[0]]
    results[r'T ratio(n)'] = ['-'] + ['%.5f'%_ for _ in trap_res[1]]
    results[r'T order(n)'] = ['-'] + ['%.5f'%_ for _ in trap_res[2]]

    results[r'$S_n(f)$'] = ['-'] + ['%.5f'%_ for _ in simp]
    results[r'S error(n)'] = ['-'] + ['%.5f'%_ for _ in simp_res[0]]
    results[r'S ratio(n)'] = ['-','-'] + ['%.5f'%_ for _ in simp_res[1]]
    results[r'S order(n)'] = ['-','-'] + ['%.5f'%_ for _ in simp_res[2]]

    table = pd.DataFrame(results) 
    table.to_latex(buf='prob5.tex',
            index=False,
            escape=False,
            column_format=9*'c',
            caption=r'Results for trapezoidal and simpson rule integrations schemes for different subdivisions on the interval $[0,\pi/2]$.',
            position='H')


