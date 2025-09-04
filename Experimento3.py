"""
Experimento 3 - Verificación de la Ley de Stefan-Boltzmann
Curso: Física Moderna 2025
Autor: Mauricio Santibañez
Descripción: Este código procesa los datos experimentales obtenidos de un filamento
de tungsteno, midiendo voltaje y corriente para calcular la resistencia y
determinar la temperatura mediante interpolación con la tabla del fabricante.
Se calcula la radiancia detectada por un sensor de radiación y se compara con la
cuarta potencia de la temperatura para verificar la ley de Stefan-Boltzmann.
Se generan gráficos de radiancia vs T^4, se realiza regresión lineal y se
propagan las incertidumbres asociadas a todas las magnitudes medidas y calculadas.
"""




import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.stats import linregress

# -----------------------------
# Datos
R_ref = 0.6  # Ω
Temperatura_Ambiente = 300 # K

Voltajes = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0])  # V
Corrientes = np.array([1.18, 1.41, 1.58, 1.75, 1.91, 2.04, 2.17, 2.30, 2.44, 2.55, 2.68])  # A
Radiancia = np.array([1.8, 3.6, 5.9, 8.6, 11.6, 14.9, 16.8, 20.5, 25.5, 29.0, 32.5])  # mV

# Tabla de conversión manual de usuario
# Cada fila: [R/R300K, Temp_K, Resistivity_μΩcm]
data = np.array([
    [1.00,  300,  5.65],
    [1.43,  400,  8.06],
    [1.87,  500, 10.56],
    [2.34,  600, 13.23],
    [2.85,  700, 16.09],
    [3.36,  800, 19.00],
    [3.88,  900, 21.94],
    [4.41, 1000, 24.93],
    [4.95, 1100, 27.94],
    [5.48, 1200, 30.98],
    [6.03, 1300, 34.08],
    [6.58, 1400, 37.19],
    [7.14, 1500, 40.36],
    [7.71, 1600, 43.55],
    [8.28, 1700, 46.78],
    [8.86, 1800, 50.05],
    [9.44, 1900, 53.35],
    [10.03, 2000, 56.67],
    [10.63, 2100, 60.06],
    [11.24, 2200, 63.48],
    [11.84, 2300, 66.91],
    [12.46, 2400, 70.39],
    [13.08, 2500, 73.91],
    [13.72, 2600, 77.49],
    [14.34, 2700, 81.04],
    [14.99, 2800, 84.70],
    [15.63, 2900, 88.33],
    [16.29, 3000, 92.04],
    [16.95, 3100, 95.76],
    [17.62, 3200, 99.54],
    [18.28, 3300, 103.3],
    [18.97, 3400, 107.2],
    [19.66, 3500, 111.1]
])

# -----------------------------
# Cálculo de Resistencias experimentales
Resistencias = Voltajes / Corrientes  # Ω

print("\n--- Resistencias calculadas ---")
for V, I, R in zip(Voltajes, Corrientes, Resistencias):
    print(f"V = {V:2.0f} V, I = {I:4.2f} A  -->  R = {R:5.2f} Ω")

# -----------------------------
# Cálculo de Temperaturas a partir de la resistencia
R_rel = Resistencias / R_ref
R_rel_tabla = data[:, 0]
Temp_tabla = data[:, 1]

interpolador_temp = interp1d(R_rel_tabla, Temp_tabla, kind='cubic', fill_value="extrapolate")
Temperaturas = interpolador_temp(R_rel)

print("\n--- Temperaturas calculadas ---")
for Rr, T in zip(R_rel, Temperaturas):
    print(f"R_rel = {Rr:4.2f}  -->  T = {T:6.1f} K")

# -----------------------------
# Cálculo de T^4 
T_cuarta = Temperaturas**4
print("\n--- Temperaturas a la cuarta potencia ---")
for T, T4 in zip(Temperaturas, T_cuarta):
    print(f"T = {T:6.1f} K  -->  T^4 = {T4:10.2e} K^4")

# -----------------------------
# Gráfico de la tabla de conversión
plt.figure(figsize=(8,5))
plt.plot(Temp_tabla, R_rel_tabla, 'b-', label='Tabla de conversión (fabricante)')
plt.plot(Temperaturas, R_rel, 'ro', label='Mediciones experimentales')
plt.xlabel('Temperatura (K)')
plt.ylabel('Resistencia relativa $R/R_{300K}$')
plt.title('Conversión de Resistencia a Temperatura del Filamento de Tungsteno')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.xlim(0, 3600)
plt.show()

# -----------------------------
# Cálculo de incertidumbres
res_Voltaje = 0.5  # V
res_Corriente = 0.01  # A
res_Radiancia = 0.1  # mV

u_res_Voltaje = res_Voltaje/np.sqrt(12)
u_res_Corriente = res_Corriente/np.sqrt(12)
u_res_Radiancia = res_Radiancia/np.sqrt(12)

print(f"\nIncertidumbre por resolución Voltímetro Analógico: {u_res_Voltaje: .2f} V")
print(f"Incertidumbre por resolución Amperímetro: {u_res_Corriente: .3f} A")
print(f"Incertidumbre por resolución Radiancia: {u_res_Radiancia: .2f} mV")

# -----------------------------
# Cálculo de incertidumbre de la resistencia
u_Resistencias = np.sqrt((1/Corrientes * u_res_Voltaje)**2 + ((-Voltajes/(Corrientes**2)) * u_res_Corriente)**2)

print("\n--- Incertidumbre de las resistencias ---")
for R, uR in zip(Resistencias, u_Resistencias):
    print(f"R = {R:5.2f} Ω  -->  u(R) = {uR:5.3f} Ω")

# -----------------------------
# Incertidumbre de R_rel 
u_R_rel = u_Resistencias / R_ref

# Derivada de T respecto a R_rel
dT_dR_rel_tabla = np.gradient(Temp_tabla, R_rel_tabla)
interpolador_deriv = interp1d(R_rel_tabla, dT_dR_rel_tabla, kind='cubic', fill_value="extrapolate")
dT_dR_rel = interpolador_deriv(R_rel)

# Incertidumbre propagada de la temperatura
u_T = dT_dR_rel * u_R_rel

print("\n--- Incertidumbre propagada de las temperaturas ---")
for T, uT in zip(Temperaturas, u_T):
    print(f"T = {T:6.1f} K  -->  u(T) = {uT:5.2f} K")

# Incertidumbre propagada de T^4
u_T_cuarta = 4 * Temperaturas**3 * u_T

print("\n--- Incertidumbre propagada de T^4 ---")
for T4_val, uT4 in zip(T_cuarta, u_T_cuarta):
    print(f"T^4 = {T4_val:10.2e} K^4  -->  u(T^4) = {uT4:10.2e} K^4")

# -----------------------------
# Regresión lineal Rad vs T^4
slope, intercept, r_value, p_value, std_err = linregress(T_cuarta, Radiancia)

# Factor de cobertura k=2 (98% confianza)
k = 2
u_T_cuarta_98 = k * u_T_cuarta
u_res_Radiancia_98 = k * u_res_Radiancia

# -----------------------------
# Gráfico con línea de ajuste
plt.figure(figsize=(8,5))
plt.errorbar(T_cuarta, Radiancia, xerr=u_T_cuarta_98, yerr=u_res_Radiancia_98, fmt='o',
             color='purple', ecolor='gray', elinewidth=1.5, capsize=3,
             label='Datos experimentales (98% conf.)')

# Línea de regresión
T_cuarta_fit = np.linspace(min(T_cuarta), max(T_cuarta), 200)
Radiancia_fit = slope * T_cuarta_fit + intercept
plt.plot(T_cuarta_fit, Radiancia_fit, 'r--', label='Ajuste por regresión lineal')

plt.xlabel('$T^4$ (K$^4$)')
plt.ylabel('Radiancia (mV)')
plt.title('Radiancia vs $T^4$ del filamento de Tungsteno')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"\nPendiente: {slope:.2e} mV/K^4")
print(f"Intercepto: {intercept:.2f} mV")
print(f"R^2: {r_value**2:.4f}")
