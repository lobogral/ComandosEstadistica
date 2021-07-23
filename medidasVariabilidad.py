def rango(muestra):
    return max(muestra)-min(muestra)

def varianza(muestra):
    media = sum(muestra)/len(muestra)
    listaMedias = [media]*len(muestra)
    cuadrados = [(x - y)**2 for x, y in zip(muestra, listaMedias)]
    return sum(cuadrados)/(len(cuadrados)-1)
    
def desviaciónEstándar(muestra):
    return varianza(muestra)**(0.5)
