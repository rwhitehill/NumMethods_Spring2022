#!/usr/bin/env python3

import numpy as np
import pandas as pd

k = np.arange(1,21)
x = 4.0**(-k)
f = np.sqrt(x**2 + 1) - 1
g = x**2/(np.sqrt(x**2 + 1) + 1)
h = x**2/2

table = pd.DataFrame({
    '$k$': k,
    '$x$': x,
    '$f(x)$': f,
    '$g(x)$': g,
    '$x^2/2$': h
    })

table.to_latex(buf='prob4_revision.tex',
        index=False,
        escape=False,
        column_format='ccccc',
        float_format="%.3e")
