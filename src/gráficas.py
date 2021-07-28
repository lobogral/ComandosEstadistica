from tiposGráficas import puntos, histograma

def dibujar(tipo, diccionarios, títuloVentana, unidadMedida):
    if tipo=="puntos":
        puntos.dibujar(diccionarios, títuloVentana, unidadMedida)
    elif tipo=="histograma":
        histograma.dibujar(diccionarios, títuloVentana, unidadMedida)