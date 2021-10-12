"""
Modulo que ofrece funcionalidades para calcular
las medidas de posicion de una muestra
"""

def media(muestra):

    """
    Calcula la media o el promedio aritmetico de una muestra

    Parametros
    ----------
    muestra: Arreglo de datos

    """

    return sum(muestra)/len(muestra)


def mediana(muestra):

    """
    Calcula la mediana de una muestra

    Parametros
    ----------
    muestra: Arreglo de datos

    """

    num_datos = len(muestra)
    muestra = sorted(muestra)
    if len(muestra) % 2 != 0:
        return muestra[(num_datos-1)//2]
    return (muestra[num_datos//2-1]+muestra[num_datos//2])/2


def media_recortada(muestra, porcentaje):

    """
    Calcula la mediana recortada de una muestra

    Parametros
    ----------
    muestra: Arreglo de datos
    porcentaje: Porcentaje de recorte

    """

    num_datos = len(muestra)
    muestra = sorted(muestra)
    num_datos_ret = round(porcentaje*num_datos)
    muestra = muestra[num_datos_ret:(num_datos - num_datos_ret)]
    return sum(muestra)/(num_datos - num_datos_ret*2)
