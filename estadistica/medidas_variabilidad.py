"""
Modulo que ofrece funcionalidades para calcular
las medidas de variabilidad de una muestra
"""

def rango(muestra):

    """
    Calcula el rango de valores en una muestra

    Parametros
    ----------
    muestra: Arreglo de datos

    """

    return max(muestra)-min(muestra)


def varianza(muestra):

    """
    Calcula la varianza de una muestra

    Parametros
    ----------
    muestra: Arreglo de datos

    """

    media = sum(muestra)/len(muestra)
    lista_medias = [media]*len(muestra)
    cuadrados = [(x - y)**2 for x, y in zip(muestra, lista_medias)]
    return sum(cuadrados)/(len(cuadrados)-1)


def desviacion_estandar(muestra):

    """
    Calcula la desviacion estandar de una muestra

    Parametros
    ----------
    muestra: Arreglo de datos

    """

    return varianza(muestra)**(0.5)
