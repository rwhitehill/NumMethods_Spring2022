#!/usr/bin/env python3

import sympy as sp

x = sp.Symbol('x')
f1 = sp.exp(x)
f2 = sp.log(x + 1)

print(sp.latex(f1.series(x,0,8)))
print()
print(sp.latex(f2.series(x,0,8)))
