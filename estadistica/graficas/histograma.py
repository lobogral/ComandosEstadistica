"""Realiza una grafica de histograma."""

from matplotlib import pyplot as plt
from redondeo.redondeo import redondear


def dibujar(diccionario: dict,
            titulo_ventana: str,
            unidad_medida: str) -> None:
    """Realiza lo descrito en el docstring del modulo.

    Parameters
    ----------
    diccionario
        Diccionario que contiene lo siguiente
        {
            "muestra": muestra,
            "paso": paso,
            "minimo": minimo,
            "maximo": maximo,
            "num_div": num_div
        }
    titulo_ventana
        Titulo de la ventana
    unidad_medida
        Unidad de la medida

    """
    muestra = diccionario['muestra']
    paso = diccionario['paso']
    minimo = diccionario['minimo']
    maximo = diccionario['maximo']
    num_div = diccionario['num_div']

    div = (maximo-minimo)/num_div

    valores_x = []
    valores_y = []
    for i in range(num_div):
        min_cls = minimo + div*i
        max_cls = minimo + div*(i+1) - paso
        frec = len([dato for dato in muestra if min_cls <= dato <= max_cls])
        valores_x += [(min_cls+max_cls)/2]
        valores_y += [redondear(frec/len(muestra), 3)]

    plt.figure(titulo_ventana)
    plt.xlabel(unidad_medida)
    plt.ylabel("Probabilidad")
    plt.bar(valores_x, valores_y, width=1, edgecolor='black')
    plt.show()
