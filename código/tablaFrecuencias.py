from decimal import Decimal, getcontext, ROUND_HALF_UP
context = getcontext()
context.rounding = ROUND_HALF_UP

def __obtenerTabla(datos, paso, mínimo, máximo, numDivisiones):
    tabla = []   
    div = (máximo-mínimo)/numDivisiones
    for i in range(numDivisiones):
        minCls = mínimo + div*i
        maxCls = mínimo + div*(i+1) - paso
        frec = len([dato for dato in datos if minCls<=dato<=maxCls])
        tabla += [{
            'intCls': f'{minCls}-{maxCls}',
            'pntMed': str((minCls+maxCls)/2),
            'frec': frec,
            'frecRel': round(Decimal(str(frec/len(datos))), 3)
        }]   
    return tabla

def imprimirTabla(datos, paso, mínimo, máximo, numDivisiones):
    tabla = __obtenerTabla(datos, paso, mínimo, máximo, numDivisiones)
    strIntCls = "Int. Cls.     "
    strPntMed = "Pnt. Med.    "
    strFrec = "Frec.    "
    strFrecRel = "Frec. Rel."
    print(f'{strIntCls}{strPntMed}{strFrec}{strFrecRel}')
    for diccionario in tabla:
        intCls = diccionario['intCls']
        pntMed = diccionario['pntMed']
        frec = diccionario['frec']
        frecRel = diccionario['frecRel']
        print(intCls, end="")
        espacios = len(strIntCls) - len(intCls) + len(str(pntMed))
        print('{:>{}}'.format(pntMed, espacios), end="")
        espacios = len(strPntMed) - len(str(pntMed)) + len(str(frec))
        print('{:>{}}'.format(frec, espacios), end="")
        espacios = len(strFrec) - len(str(frec)) + len(str(frecRel))
        print('{:>{}}'.format(frecRel, espacios))

def establecerDatosHist(datos, paso, mínimo, máximo, numDivisiones):
    tabla = __obtenerTabla(datos, paso, mínimo, máximo, numDivisiones)
    hist = {}
    hist['valoresx'] = [diccionario['pntMed'] for diccionario in tabla]
    hist['valoresy'] = [diccionario['frecRel'] for diccionario in tabla]
    return hist