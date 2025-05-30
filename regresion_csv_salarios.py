# -*- coding: utf-8 -*-
"""regresion_csv_salarios.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cr4vrBdsYdqriCVK7jzUD2--cB-p3nVk
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer los datos desde la URL
url = "https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv"
datos = pd.read_csv(url)

# Separar columnas
x = datos.iloc[:, 0].values  # Experiencia
y = datos.iloc[:, 1].values  # Salario

# Cálculo de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

print(f"Función de regresión lineal: Salario = {a0:.2f} + {a1:.2f} * Experiencia")

# Estimar salarios para 15, 30 y 50 años
experiencias = [15, 30, 50]
for e in experiencias:
    salario_estimado = a0 + a1 * e
    print(f"Para {e} años de experiencia, salario estimado = ${salario_estimado:.2f}")

# Gráfica
plt.scatter(x, y, color='red', label='Datos reales')
plt.plot(x, a0 + a1 * x, label='Recta de regresión', color='blue')
plt.xlabel('Experiencia en años')
plt.ylabel('Salario')
plt.title('Regresión Lineal: Experiencia vs Salario')
plt.legend()
plt.grid()
plt.show()