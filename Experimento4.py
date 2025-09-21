"""
Experimento 4 - Medición de la Velocidad de la Luz en el Aire
Curso: Física Moderna 2025
Autor: Mauricio Santibañez
Descripción: Este código procesa los datos experimentales de desfase temporal (Δt) y distancia recorrida (Δd)
medidos con un láser, un espejo y un fotoreceptor conectado a un osciloscopio. Realiza un ajuste lineal
de Δd vs Δt para determinar la velocidad de la luz en el aire, calcula la incertidumbre asociada al 
valor de c mediante propagación de errores, y genera gráficos que muestran los datos experimentales
y la recta de ajuste correspondiente.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Datos experimentales
fases = np.array([208.0e-9, 211.0e-9, 216.0e-9, 221.0e-9, 225.0e-9, 230.0e-9])  # s
distancias = np.array([16.82, 17.82, 18.82, 19.82, 20.82, 21.82])               # m

# ===============================
# Resoluciones de los instrumentos
res_fase = 0.1e-9   # s
res_huincha = 0.05  # m

# ===============================
# Incertidumbres 
u_dt = res_fase / np.sqrt(12)  # s
u_dd = res_huincha / np.sqrt(12)  # m

# ===============================
# Ajuste lineal 
slope, intercept, r_value, p_value, std_err = linregress(fases, distancias)

print(f"Pendiente (c) = {slope:.2e} m/s")
print(f"Intercepto = {intercept:.2f} m")
print(f"R² = {r_value**2:.4f}")

# ===============================
# Propagación de incertidumbre
d_prom = np.mean(distancias)
t_prom = np.mean(fases)

u_c = np.sqrt((u_dd / t_prom) ** 2 + (d_prom * u_dt / t_prom**2) ** 2)

print(f"Incertidumbre de c = {u_c:.2e} m/s")

# ===============================
# Gráfico
plt.figure(figsize=(8, 5))
plt.scatter(fases * 1e9, distancias, color='blue', label='Datos experimentales')
plt.plot(
    fases * 1e9,
    slope * fases + intercept,
    color='red',
    label=(f"Ajuste lineal:\n"
           f"Δd = {slope:.2e}Δt + {intercept:.2f}\n"
           f"c = ({slope:.2e} ± {u_c:.2e}) m/s")
)

plt.xlabel("Δt (ns)")
plt.ylabel("Δd (m)")
plt.title("Medición de la velocidad de la luz")
plt.legend()
plt.grid(True)
plt.show()
