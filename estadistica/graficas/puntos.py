"""Realiza una grafica de puntos unidimensional."""

from matplotlib import pyplot as plt


def dibujar(diccionarios: list[dict],
            titulo_ventana: str,
            unidad_medida: str) -> None:
    """Realiza lo descrito en el docstring del modulo.

    Parameters
    ----------
    diccionarios
        Lista de diccionarios con la siguiente estructura
        {
            'nombre': nombre,
            'color': color,
            'muestra': muestra
        }
    titulo_ventana
        Titulo de la ventana
    unidad_medida
        Unidad de la medida

    """
    muestras = [val for dic in diccionarios for val in dic['muestra']]
    limite_superior = __establecer_limite_superior(muestras)
    listas_y = __establecer_valores_y(muestras, len(diccionarios))

    plt.figure(titulo_ventana, figsize=(9, 0.9+0.15*limite_superior))
    for diccionario, lista_y in zip(diccionarios, listas_y):
        color = diccionario['color']
        valores_x = diccionario['muestra']
        valores_y = lista_y
        label = diccionario['nombre'] if len(diccionarios) > 1 else ""
        plt.hlines(0, min(valores_x), max(valores_x), colors='k')
        plt.plot(valores_x, valores_y, 'o', color=color, label=label)
    if len(diccionarios) > 1:
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xlabel(unidad_medida)
    plt.ylim(-1, limite_superior)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()


def __establecer_valores_y(muestras: list,
                           num_diccs: int) -> list[list]:
    """Establece lista de valores 'y' de la grafica.

    Parameters
    ----------
    muestras
        Lista de todos los valores de la muestras
    num_diccs
        Numero de diccionarios

    Returns
    -------
    list[list]
        Lista que contiene una lista por cada muestra

    """
    vals_x = muestras
    vals_y = [vals_x[0:i+1].count(vals_x[i])-1 for i in range(len(vals_x))]
    num_elem = len(vals_y)//num_diccs
    return [vals_y[i:i+num_elem] for i in range(0, len(vals_y), num_elem)]


def __establecer_limite_superior(muestras: list) -> int:
    """Calcula el limite superior de la grafica.

    Parameters
    ----------
    muestras
        Lista de todos los valores de la muestras

    Returns
    -------
    int
        Limite superior

    """
    return max([muestras.count(val) for val in muestras])
