# -*- coding: utf-8 -*-
"""MetodoNewtonRaphson.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10U-_Mo86g7hK-PzbIm8lh27ZsaPuxWmA
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 8*x*np.sin(x)*np.exp(-x) - 1
f_prima = lambda x: 8*np.sin(x)*np.exp(-x) + 8*x*np.cos(x)*np.exp(-x) - 8*x*np.sin(x)*np.exp(-x)

x0 = 0.3
n = 5

iteraciones = []

for i in range(n):

    x_nueva = x0 - f(x0) / f_prima(x0)

    if i > 0:
        error_r = abs((x_nueva - x0) / x_nueva)
    else:
        error_r = None

    iteraciones.append([i+1, round(x_nueva, 4), round(error_r, 4) if error_r is not None else 'N/A'])

    x0 = x_nueva

print("\nTabla de resultados:")
print(f"{'Iteración':<12}{'Raíz Estimada':<18}{'Error Relativo (εr)'}")
for it in iteraciones:
    print(f"{it[0]:<12}{it[1]:<18}{it[2]}")

x_vals = np.linspace(0, 2, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = 8x*sin(x)*e^(-x) - 1")
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(x0, f(x0), color='red', label=f"Raíz estimada: {round(x0, 4)}", zorder=5)
plt.title("Gráfica de la función y la raíz estimada")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()