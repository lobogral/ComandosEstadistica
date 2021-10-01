def media(muestra):
    return sum(muestra)/len(muestra)

def mediana(muestra):
    n = len(muestra)
    muestra = sorted(muestra)
    if len(muestra) % 2 != 0:
        return muestra[(n-1)//2]
    else:
        return (muestra[n//2-1]+muestra[n//2])/2
    
def media_recortada(muestra, porcentaje):
    n = len(muestra)
    muestra = sorted(muestra)
    num_datos_retirados = round(porcentaje*n)
    muestra = muestra[num_datos_retirados:(n - num_datos_retirados)]
    return sum(muestra)/(n - num_datos_retirados*2)