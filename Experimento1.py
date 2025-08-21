"""
Experimento 1 - Radiación Infrarroja y Ley de Stefan-Boltzmann
Curso: Física Moderna 2025
Autor: Mauricio Santibañez
Descripción: Este código procesa datos experimentales de radiación térmica,
y genera gráficos comparativos con datos reales medidos en clase.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos
R = np.array([2041.7, 2157.6, 2281.0, 2412.6, 2553.0, 2702.7, 2862.5, 3033.3, 3215.8, 3411.0,
              3619.8, 3843.4, 4082.9, 4339.7, 4615.1, 4910.7, 5228.1, 5569.3, 5936.1, 6330.8,
              6755.9, 7214.0, 7707.7, 8240.6, 8816.0, 9437.7, 10100, 10837, 11625, 12479, 
              13405, 14410, 15502, 16689, 17980, 19386, 20919, 22590, 24415, 26409, 28590,
              30976, 33591, 36458, 39605, 43062, 46863, 51048, 55658, 60743, 66356, 72560, 79422])

T_C = np.array([134 - 2*i for i in range(53)])  # °C
T_K = T_C + 273.15  # Kelvin

# --- Coeficientes dados Steinhart-Hart ---
A = 8.467428050163e-4
B = 2.058325204985e-4
C = 9.050118014518e-8

# --- Modelo Steinhart-Hart ---
def steinhart(R):
    return 1.0 / (A + B*np.log(R) + C*(np.log(R)**3))

# Valores ajustados con tus coeficientes
T_fit_SH = steinhart(R)

# --- Interpolación spline cúbico ---
spline = interp1d(R, T_K, kind="cubic")

# --- Graficar ---
plt.figure(figsize=(8,5))
plt.scatter(R, T_K, label="Datos tabla", color="blue")
plt.plot(R, spline(R), "--", label="Spline cúbico", color="green")
plt.plot(R, T_fit_SH, label="Steinhart-Hart (coef. dados)", color="red")
plt.xlabel("Resistencia [Ω]")
plt.ylabel("Temperatura [K]")
plt.title("Comparación spline vs Steinhart-Hart")
plt.legend()
plt.grid()
plt.show()



#------------------------------------------------------------------------------------------

#Datos Resoluciones y temperatura ambiente
res_Voltimetro = 0.1 #mV 
res_Ohmetro = 0.01 #kOhms

Temperatura_ambiente = 23 + 273.15 #K 


#------------------------------------------------------------------------------------------

#Mediciones para incertidumbre tipo A:

#Potencia 9 

R9_repetibilidad = 2.28 #KOhms
V9_repetibilidad = [28.6, 28.7, 28.6, 28.6, 28.6, 28.6, 28.7, 28.6] #mV

#Potencia 7

R7_repetibilidad = 2.69 #KOhms
V7_repetibilidad = [25.7, 25.6 ,25.7, 25.6, 25.6, 25.6, 25.5, 25.6] #mV

#Potencia 6

R6_repetibilidad = 3.76 #KOhms 
V6_repetibilidad = [21.3, 21.3, 21.3, 21.3, 21.3, 21.2, 21.3, 21.4] #mV 

#Potencia 5

R5_repetibilidad = 6.54 #KOhms
V5_repetibilidad = [15.5, 15.5, 15.5, 15.5, 15.4, 15.5, 15.5, 15.5] #mV

#------------------------------------------------------------------------------------------

#Cálculo de incertidumbres 

# -- Por resolución --

u_res_V = res_Voltimetro / np.sqrt(12)
u_res_Ohm = res_Ohmetro / np.sqrt(12)

# -- Tipo A -- 

n_V = 8

std_V9 = np.std(V9_repetibilidad)
std_V7 = np.std(V7_repetibilidad)
std_V6 = np.std(V6_repetibilidad)
std_V5 = np.std(V5_repetibilidad)

u_A_V9 = std_V9/np.sqrt(n_V)
u_A_V7 = std_V7/np.sqrt(n_V)
u_A_V6 = std_V6/np.sqrt(n_V)
u_A_V5 = std_V5/np.sqrt(n_V)

#Mostrar Resultados 
print("Incertidumbre por resolución Voltímetro:", u_res_V, "mV")
print("Incertidumbre por resolución Ohmetro:", u_res_Ohm, "kOhms")

print("Incertidumbre tipo A Potencia 9:", u_A_V9, "mV")
print("Incertidumbre tipo A Potencia 7:", u_A_V7, "mV")
print("Incertidumbre tipo A Potencia 6:", u_A_V6, "mV")
print("Incertidumbre tipo A Potencia 5:", u_A_V5, "mV")

print("Incertidumbre combinada Potencia 9:", np.sqrt(u_res_V**2 + u_A_V9**2), "mV")
print("Incertidumbre combinada Potencia 7:", np.sqrt(u_res_V**2 + u_A_V7**2), "mV")
print("Incertidumbre combinada Potencia 6:", np.sqrt(u_res_V**2 + u_A_V6**2), "mV")
print("Incertidumbre combinada Potencia 5:", np.sqrt(u_res_V**2 + u_A_V5**2), "mV")
#------------------------------------------------------------------------------------------

#Mediciones Realizadas 

#Potencia 9

R9_negra = 2.18 #kOhms 
V9_negra = 28.6 #mV

R9_blanca = 2.18 #kOhms
V9_blanca = 27.9 #mV     

R9_bruñido = 2.18 #kOhms 
V9_bruñido = 8.9 #mV

R9_pulido = 2.18 #kOhms 
V9_pulido = 1.4 #mV

#Potencia 7

R7_negra = 2.75 #kOhms 
V7_negra = 25.1 #mV

R7_blanca = 2.75 #kOhms
V7_blanca = 24.5 #mV     

R7_bruñido = 2.75 #kOhms 
V7_bruñido = 7.8 #mV

R7_pulido = 2.75 #kOhms 
V7_pulido = 1.3 #mV

#Potencia 6

R6_negra = 3.87 #kOhms 
V6_negra = 20.8 #mV

R6_blanca = 3.87 #kOhms
V6_blanca = 20.5 #mV     

R6_bruñido = 3.87 #kOhms 
V6_bruñido = 6.5 #mV

R6_pulido = 3.87 #kOhms 
V6_pulido = 1.2 #mV

#Potencia 5

R5_negra = 6.60 #kOhms 
V5_negra = 15.3 #mV

R5_blanca = 6.60 #kOhms
V5_blanca = 15.1 #mV     

R5_bruñido = 6.60 #kOhms 
V5_bruñido = 4.7 #mV

R5_pulido = 6.60 #kOhms 
V5_pulido = 0.9 #mV

#------------------------------------------------------------------------------------------

#Conversión Resistencia a Temperatura con resolución considerada

#Diccionario con las resistencias medidas en Ohms
resistencias = {
    "R9": {"negra": R9_negra*1000, "blanca": R9_blanca*1000, "bruñido": R9_bruñido*1000, "pulido": R9_pulido*1000},
    "R7": {"negra": R7_negra*1000, "blanca": R7_blanca*1000, "bruñido": R7_bruñido*1000, "pulido": R7_pulido*1000},
    "R6": {"negra": R6_negra*1000, "blanca": R6_blanca*1000, "bruñido": R6_bruñido*1000, "pulido": R6_pulido*1000},
    "R5": {"negra": R5_negra*1000, "blanca": R5_blanca*1000, "bruñido": R5_bruñido*1000, "pulido": R5_pulido*1000},
}

#Calcular temperaturas usando spline y redondear según resolución del Ohmetro (0.01 kΩ)
temperaturas = {}
for potencia, caras in resistencias.items():
    temperaturas[potencia] = {}
    for cara, R_val in caras.items():
        T_K = float(spline(R_val))  # Temperatura en Kelvin
        T_K_redondeada = round(T_K, 1)  # redondear 0.1 K, ejemplo de resolución práctica
        temperaturas[potencia][cara] = T_K_redondeada

#Resultados
for potencia, caras in temperaturas.items():
    print(f"\nTemperaturas para {potencia}:")
    for cara, T_K in caras.items():
        print(f"{cara}: {T_K} K")


#Resistencias repetibilidad convertidas a Ohms
repetibilidad = {
    "R9": R9_repetibilidad*1000,
    "R7": R7_repetibilidad*1000,
    "R6": R6_repetibilidad*1000,
    "R5": R5_repetibilidad*1000,
}

# Calcular temperaturas de repetibilidad
temp_repetibilidad = {}
for potencia, R_val in repetibilidad.items():
    T_K = float(spline(R_val))
    temp_repetibilidad[potencia] = round(T_K, 1)

#Resultados
print("\nTemperaturas de repetibilidad:")
for potencia, T_K in temp_repetibilidad.items():
    print(f"{potencia}: {T_K} K")



#Comparación máxima diferencia spline vs Steinhart-Hart
diferencias = np.abs(spline(R) - T_fit_SH)
max_diferencia = np.max(diferencias)
indice_max = np.argmax(diferencias)

print(f"\nMáxima diferencia entre spline y Steinhart-Hart: {max_diferencia:.3f} K")
print(f"Se produce en R = {R[indice_max]} Ω, T_spline = {spline(R[indice_max]):.3f} K, T_SH = {T_fit_SH[indice_max]:.3f} K")

#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------

#Organizar mediciones en arrays
potencias = ["R9", "R7", "R6", "R5"]
caras = ["negra", "blanca", "bruñido", "pulido"]

# Tensiones medidas
V_medidas = {
    "R9": [V9_negra, V9_blanca, V9_bruñido, V9_pulido],
    "R7": [V7_negra, V7_blanca, V7_bruñido, V7_pulido],
    "R6": [V6_negra, V6_blanca, V6_bruñido, V6_pulido],
    "R5": [V5_negra, V5_blanca, V5_bruñido, V5_pulido],
}

# Temperaturas correspondientes (ya calculadas con spline)
T_medidas = {pot: [temperaturas[pot][c] for c in caras] for pot in potencias}

#V vs T para cada superficie ---
plt.figure(figsize=(8,6))
for i, cara in enumerate(caras):
    T_vals = [T_medidas[pot][i] for pot in potencias]
    V_vals = [V_medidas[pot][i] for pot in potencias]
    plt.plot(T_vals, V_vals, "o-", label=f"Cara {cara}")
plt.xlabel("Temperatura [K]")
plt.ylabel("Voltaje termopila [mV]")
plt.title("Señal de radiación vs Temperatura")
plt.legend()
plt.grid()
plt.show()

# Emisividades relativas normalizadas a la cara negra
plt.figure(figsize=(8,6))
for pot in potencias:
    V_vals = np.array(V_medidas[pot])
    V_norm = V_vals / V_vals[0]  # normalizar respecto a la cara negra
    # Cambiar R- por P- en etiquetas
    plt.bar([f"P{pot[-1]}-{c}" for c in caras], V_norm, label=f"P{pot[-1]}")
plt.axhline(1.0, color="k", linestyle="--", linewidth=0.8)
plt.xlabel("Potencia asociada")  # nueva etiqueta del eje X
plt.ylabel("Emisividad relativa (ε/ε_negra)")
plt.title("Comparación de emisividades relativas")
plt.xticks(rotation=45)
plt.ylim(0, 1.1)
plt.grid(axis="y", linestyle=":")
plt.legend(title="Nivel de potencia")
plt.show()
