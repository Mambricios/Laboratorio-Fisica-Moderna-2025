"""
Experimento 2 - Ley del Inverso del Cuadrado para Radiación Infrarroja
Curso: Física Moderna 2025
Autor: Mauricio Santibañez
Descripción: Este código procesa datos experimentales de voltaje medido por un sensor
de radiación infrarroja frente a una fuente puntual. Genera gráficos de repetibilidad,
voltaje vs distancia y voltaje vs 1/r², y calcula las incertidumbres asociadas
a las mediciones y la propagación para 1/r².
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# -----------------------------
# Datos
distancias = np.array([3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50])
voltaje = np.array([92.0, 37.2, 29.7, 23.4, 21.0, 15.5, 11.9, 9.0, 7.4, 6.2, 2.8, 1.4, 0.8, 0.4, 0.1, 0])

# 1/r^2
distancias_inverso = 1 / (distancias**2)

# Repetibilidad (mV)
repetibilidad = np.array([6.2, 6.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.6]) 

# -----------------------------
# Gráfico 1: Repetibilidad 
plt.figure(figsize=(7,5))
plt.bar(range(1, len(repetibilidad)+1), repetibilidad, color="skyblue", edgecolor="black", alpha=0.7, label="Mediciones")
plt.axhline(np.mean(repetibilidad), color="red", linestyle="--", label=f"Media = {np.mean(repetibilidad):.2f} mV")
plt.title("Repetibilidad de mediciones de voltaje")
plt.xlabel("Número de medición")
plt.ylabel("Voltaje [mV]")
plt.legend()
plt.grid(True, alpha=0.4)
plt.show()

# -----------------------------
# Gráfico 2: Voltaje vs Distancia
plt.figure(figsize=(7,5))
plt.plot(distancias, voltaje, "o", label="Datos medidos")

# Interpolación 
interp = interp1d(distancias, voltaje, kind="cubic")
x_smooth = np.linspace(min(distancias), max(distancias), 300)
plt.plot(x_smooth, interp(x_smooth), "-", alpha=0.7)

plt.title("Voltaje medido vs Distancia")
plt.xlabel("Distancia [cm]")
plt.ylabel("Voltaje [mV]")
plt.legend()
plt.grid(True, alpha=0.4)
plt.show()

# -----------------------------
# Gráfico 3: Voltaje vs 1/r^2 
plt.figure(figsize=(7,5))
plt.plot(distancias_inverso, voltaje, "o", label="Datos medidos")
plt.plot(distancias_inverso, voltaje, "-", color="red", alpha=0.7, label="Conexión de puntos")

plt.title("Voltaje medido vs 1/r²")
plt.xlabel("1 / Distancia² [1/cm²]")
plt.ylabel("Voltaje [mV]")
plt.legend()
plt.grid(True, alpha=0.4)
plt.show()

# -----------------------------
# Cálculo de incertidumbres
# Definir resolución de voltímetro y huincha
res_Voltimetro = 0.1  #mV
res_huincha = 0.1     #cm

# -- Por resolución --
u_res_V = res_Voltimetro / np.sqrt(12)
u_res_huincha = res_huincha / np.sqrt(12)

# -- Tipo A --
n_V = len(repetibilidad)
std_V = np.std(repetibilidad, ddof=1)
u_A_V = std_V / np.sqrt(n_V)

# Mostrar resultados
print(f"Incertidumbre por resolución Voltímetro: {u_res_V: .2f} mV")
print(f"Incertidumbre por resolución huincha: {u_res_huincha: .2f} cm")
print(f"Incertidumbre tipo A Voltaje: {u_A_V: .2f} mV")
print(f"Incertidumbre combinada: {np.sqrt(u_res_V**2 + u_A_V**2): .2f} mV")

# -----------------------------
# Incertidumbre representativa para 1/r^2 usando r_media
r_media = np.mean(distancias)
u_propagacion = np.sqrt(((2 / r_media**3)**2 * u_res_huincha**2))

print(f"r_media = {r_media:.1f} cm")
print(f"Incertidumbre representativa u(1/r^2) = {u_propagacion:.5f} cm^-2")
