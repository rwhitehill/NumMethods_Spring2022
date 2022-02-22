#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def bisection(f,a,b,M=1e5,delta=1e-10,eps=1e-10):
    u = f(a)
    v = f(b)
    c = (a+b)/2
    m = f(c)
    for i in range(int(M)):
        if abs(a-b) < delta or abs(m) < eps:
            break
        if f(a)*f(c) < 0:
            b = c
            v = m
        else:
            a = c
            u = m
        c = (a+b)/2
        m = f(c)
    return c

m = [7,13,17]
root_m = []
s = 2.0
for i in range(len(m)):
    f = lambda x: x**2-m[i]
    a = s
    b = s+1
    root_m.append(bisection(f,a,b,M=7))
    s += 1

print(root_m)

