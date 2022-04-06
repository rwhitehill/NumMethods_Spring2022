#!/usr/bin/env python3

import numpy as np
import pandas as pd

k = np.arange(1,21)
x = 4.0**(-k)
f = np.sqrt(x**2 + 1) - 1
g = x**2/(np.sqrt(x**2 + 1) + 1)

table = pd.DataFrame({
    '$k$': k,
    '$x$': x,
    '$f(x)$': f,
    '$g(x)$': g
    })

table.to_latex(buf='prob4.tex',
        index=False,
        escape=False,
        column_format='cccc',
        float_format="%.3e")
