"""
Realiza una grafica de histograma
"""

from matplotlib import pyplot as plt


def dibujar(diccionarios, titulo_ventana, unidad_medida):

    """
    Realiza lo descrito en el docstring del modulo

    Parametros
    ----------
    diccionarios: Diccionarios que contiene
    - nombre: Nombre de la muestra
    - color: Color de los puntos
    - muestra: Arreglo de datos
    titulo_ventana: Titulo de la ventana
    unidad_medida: Unidad de la medida

    """

    plt.figure(titulo_ventana)
    plt.xlabel(unidad_medida)
    plt.ylabel("Probabilidad")
    valores_x = diccionarios['valores_x']
    valores_y = diccionarios['valores_y']
    plt.bar(valores_x, valores_y, width=1, edgecolor='black')
    plt.show()
