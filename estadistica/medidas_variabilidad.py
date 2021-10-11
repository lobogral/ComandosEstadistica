def rango(muestra):
    return max(muestra)-min(muestra)


def varianza(muestra):
    media = sum(muestra)/len(muestra)
    lista_medias = [media]*len(muestra)
    cuadrados = [(x - y)**2 for x, y in zip(muestra, lista_medias)]
    return sum(cuadrados)/(len(cuadrados)-1)


def desviacion_estandar(muestra):
    return varianza(muestra)**(0.5)
