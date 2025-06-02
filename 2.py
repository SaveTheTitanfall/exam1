import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
# 4 nevidomuh
a_values = np.arange(-20, 20)
results = []
variables = ['x1', 'x2', 'x3', 'x4']

for a in a_values:
    A = np.array([
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [a, 1, -1, 2],
        [1, a, 1, -1]
    ])
    b = np.array([10, 10, a, -a])
    
    try:
        x = np.linalg.solve(A, b)
        results.append(x)
    except np.linalg.LinAlgError:
        results.append([np.nan] * 4)

df = pd.DataFrame(results, columns=variables, index=a_values)
df.index.name = 'a'
print(df)

plt.figure(figsize=(12, 6))
for var in variables:
    plt.plot(df.index, df[var], label=var, marker='o')
plt.title("zal vid  a")
plt.xlabel("a")
plt.ylabel("znach perem")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()