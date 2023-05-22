import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
from valoresdeentrada import valoresdeentrada

def function_granulometria():
    granulometria, suelo = valoresdeentrada()

    # Curva granulométrica.
    plt.figure(figsize=(10, 5))
    plt.plot(granulometria["Abertura (mm)"], granulometria["Porcentaje_pasa"], marker='o', markerfacecolor='limegreen',
             color='darkgreen')
    granulometria["Abertura (mm)"]

    # Para el título se establece un cuadro perimetral sin relleno de color negro.
    plt.title("CURVA GRANULOMÉTRICA", bbox=dict(facecolor='none', edgecolor='k', boxstyle='round,pad=0.2'))

    # Color y escala, configuración de la grilla logarítmica.
    plt.grid(which='major', axis='y', color='k', ls='solid', lw=.3)
    plt.grid(which='minor', axis='x', color='k', ls='solid', lw=.3)
    plt.xscale('log')

    # El siguiente comando permite invertir el eje x, con el objeto de observar correctamente la curva granulométrica.
    plt.gca().invert_xaxis()

    # Etiquetas de los ejes x e y
    plt.xlabel("Tamaño de partícula (mm)", fontsize=12)
    plt.ylabel("Porcentaje que pasa el tamiz", fontsize=12)

    # Líneas de referencia horizontales y verticales en color naranja
    plt.axvline(0.075, color="orange", linewidth=1, linestyle="--")
    plt.axvline(4.75, color="orange", linewidth=1, linestyle="--")
    plt.axhline(10, color="orange", linewidth=1, linestyle="--")
    plt.axhline(30, color="orange", linewidth=1, linestyle="--")
    plt.axhline(60, color="orange", linewidth=1, linestyle="--")

    # Etiquetas para las líneas de referencia y para los diámetros solicitados en color verde oscuro
    plt.text(5.6, 80, 'Tamiz No. 4', fontsize=12, color='darkgreen')
    plt.text(0.19, 80, 'Tamiz No. 200', fontsize=12, color='darkgreen')
    plt.text(20, 61, 'Diámetro D-60', fontsize=12, color='darkgreen')
    plt.text(20, 31, 'Diámetro D-30', fontsize=12, color='darkgreen')
    plt.text(20, 11, 'Diámetro D-10', fontsize=12, color='darkgreen')

    # Mostrar la gráfica
    plt.show()

    # Datos experimentales
    D = np.array([0.3, 0.6, 1.18, 2.36, 4.75, 9.5, 19])
    K = np.array([0.01, 0.027, 0.072, 0.202, 0.442, 1.06, 2.48])

    # Interpolación
    f = interp1d(K, D, kind='cubic')
    # Creamos las variables que dan a conocer los tamaños donde pasan los porcentajes de paso del 60%, 30% y 10%
    tamaño_D60 = f(0.6)
    tamaño_D30 = f(0.3)
    tamaño_D10 = f(0.1)
    # Imprimimos los valores de los diámetros de los porcentajes de paso que necesitamos
    print("D60 = {:.2f} mm".format(tamaño_D60))
    print("D30 = {:.2f} mm".format(tamaño_D30))
    print("D10 = {:.2f} mm".format(tamaño_D10))

    # Coeficiente de uniformidad Cu.
    Cu = tamaño_D60 / tamaño_D10
    # Coeficiente de curvatura Cc.
    Cc = (tamaño_D30 ** 2) / (tamaño_D60 * tamaño_D10)

    # En la impresión de los datos calculados se ha usado el comando f"{variable:.3f}" el cual permite definir el número de posiciones decimales que se mostrarán al usuario (en este caso 3).
    print(f"{Cu:.3f}", ": Coeficiente de uniformidad.")
    print(f"{Cc:.3f}", ": Coeficiente de curvatura.")
    
    # Crear el diccionario con los resultados
    resultados = {"Cc": Cc, "Cu": Cu}
    return resultados

# Llamar a la función para mostrar la gráfica y obtener los resultados
resultados_granulometria = function_granulometria()

# Obtener los valores de Cc y Cu desde los resultados
Cc = resultados_granulometria["Cc"]
Cu = resultados_granulometria["Cu"]