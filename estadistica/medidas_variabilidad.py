"""Calcula medidas de variabilidad de una muestra."""
from typing import Union


def rango(muestra: list[Union[int, float]]) -> Union[float, int]:
    """Calcula el rango de valores en una muestra.

    Parametros
    ----------
    muestra
        Arreglo de datos

    Returns
    -------
    float | int
        Rango

    """
    return max(muestra)-min(muestra)


def varianza(muestra: list[Union[int, float]]) -> float:
    """Calcula la varianza de una muestra.

    Parametros
    ----------
    muestra
        Arreglo de datos

    Returns
    -------
    float
        Varianza

    """
    media = sum(muestra)/len(muestra)
    lista_medias = [media]*len(muestra)
    cuadrados = [(x - y)**2 for x, y in zip(muestra, lista_medias)]
    return sum(cuadrados)/(len(cuadrados)-1)


def desviacion_estandar(muestra: list[Union[int, float]]) -> float:
    """Calcula la desviacion estandar de una muestra.

    Parametros
    ----------
    muestra
        Arreglo de datos

    Returns
    -------
    float
        Desviacion

    """
    return varianza(muestra)**(0.5)
