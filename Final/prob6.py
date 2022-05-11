#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Euler(F,y0,a,b,h):
    t = [a]; w = [y0]
    while t[-1] < b:
        w.append(w[-1] + h*F(t[-1],w[-1]))
        t.append(t[-1] + h)
    t = np.array(t); w = np.array(w)
    return t,w

def Taylor2(F,Fp,y0,a,b,h):
    t = [a]; w = [y0]
    while t[-1] < b:
        w.append(w[-1] + h*(F(t[-1],w[-1]) + h/2.0*Fp(t[-1],w[-1])))
        t.append(t[-1] + h)
    t = np.array(t); w = np.array(w)
    return t,w

def RK2(F,y0,a,b,h):
    t = [a]; w = [y0]
    while t[-1] < b:
        k1 = F(t[-1],w[-1])
        k2 = F(t[-1]+h/2.0,w[-1]+h*k1/2.0)
        w.append(w[-1] + h*k2)
        t.append(t[-1] + h)
    t = np.array(t); w = np.array(w)
    return t,w

def error(approx):
    exact = y(1.0)
    return abs(exact - approx) 

def order(errors):
    num = errors[:-1]
    den = errors[1:]
    return np.log2(num/den) 

def get_results(approx):
    errors = error(approx)
    orders = order(errors)
    return errors,orders

if __name__ == '__main__':

    F  = lambda t,y: -10.0 * y**2.0
    Fp = lambda t,y: 200.0 * y**3.0
    a = 0.0; b = 1.0
    y0 = 1
    
    y = lambda t: 1.0/(10.0 * t + 1.0)

    H = [1.0/(10.0 * 2.0**float(i)) for i in range(1,6)]
   
    sub_heads = [r'${\rm error}(h)$',r'${\rm order}(h)$']

    col = ['$1/20$','$1/40$','$1/80$','$1/160$','$1/320$']
    h_col = pd.DataFrame(col,columns=['$h$'])
   
    e = []
    temp = np.array([Euler(F,y0,a,b,_)[1][-1] for _ in H])
    res = get_results(temp)
    #e.append(['%.4f'%_ for _ in temp])
    e.append(['%.5f'%_ for _ in res[0]])
    e.append(['-'] + ['%.5f'%_ for _ in res[1]])
    e = np.array(e).T
    e = pd.DataFrame(e,columns=sub_heads)
    
    t = []
    temp = np.array([Taylor2(F,Fp,y0,a,b,_)[1][-1] for _ in H])
    res = get_results(temp)
    #t.append(['%.4f'%_ for _ in temp])
    t.append(['%.5f'%_ for _ in res[0]])
    t.append(['-'] + ['%.5f'%_ for _ in res[1]])
    t = np.array(t).T
    t = pd.DataFrame(t,columns=sub_heads)
   
    r = []
    temp = np.array([RK2(F,y0,a,b,_)[1][-1] for _ in H])
    res = get_results(temp)
    #r.append(['%.4f'%_ for _ in temp])
    r.append(['%.5f'%_ for _ in res[0]])
    r.append(['-'] + ['%.5f'%_ for _ in res[1]])
    r = np.array(r).T
    r = pd.DataFrame(r,columns=sub_heads)

    table = pd.concat({r'$\phantom{h}$':h_col,'Euler':e,'Taylor':t,'Runge Kutta':r},
            axis=1)
    table = table.reset_index(drop=True)
    table = table.set_index([[''] * table.shape[0]])
    tex_output = table.to_latex(index=True,
            escape=False,
            column_format=table.shape[1]*'c',
            multicolumn_format='c',
            caption=r'Accuracy table at $t=1$ with different ODE approximation schemes, where the exact value is $y(1) = 1/11$.',
            position='H')
    tex_output = tex_output.replace('{} &','')

    with open('./prob6.tex','w') as f:
        f.write(tex_output)
    
