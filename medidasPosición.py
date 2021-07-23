def media(muestra):
    return sum(muestra)/len(muestra)

def mediana(muestra):
    n = len(muestra)
    muestra = sorted(muestra)
    if len(muestra) % 2 != 0:
        return muestra[(n-1)//2]
    else:
        return (muestra[n//2-1]+muestra[n//2])/2
    
def mediaRecortada(muestra, porcentaje):
    n = len(muestra)
    muestra = sorted(muestra)
    numDatosRetirados = round(porcentaje*n)
    muestra = muestra[numDatosRetirados:(n - numDatosRetirados)]
    return sum(muestra)/(n - numDatosRetirados*2)
