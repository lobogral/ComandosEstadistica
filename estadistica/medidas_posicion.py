"""Calcula medidas de posición de una muestra."""
from typing import Union


def media(muestra: list[Union[int, float]]) -> float:
    """Calcula el promedio aritmético de una muestra.

    Parameters
    ----------
    muestra
        Arreglo de datos

    Returns
    -------
    float
        Media

    """
    return sum(muestra)/len(muestra)


def mediana(muestra: list[Union[int, float]]) -> Union[float, int]:
    """Calcula la mediana de una muestra.

    Parameters
    ----------
    muestra
        Arreglo de datos

    Returns
    -------
    float | int
        Mediana

    """
    num_datos = len(muestra)
    muestra = sorted(muestra)
    if len(muestra) % 2 != 0:
        return muestra[(num_datos-1)//2]
    return (muestra[num_datos//2-1]+muestra[num_datos//2])/2


def media_recortada(muestra: list[Union[int, float]],
                    porcentaje: float) -> float:
    """Calcula la mediana recortada de una muestra.

    Parameters
    ----------
    muestra
        Arreglo de datos
    porcentaje
        Porcentaje de recorte

    Returns
    -------
    float
        Media recortada

    """
    num_datos = len(muestra)
    muestra = sorted(muestra)
    num_datos_ret = round(porcentaje*num_datos)
    muestra = muestra[num_datos_ret:(num_datos - num_datos_ret)]
    return sum(muestra)/(num_datos - num_datos_ret*2)
