from matplotlib import pyplot as plt

def dibujar(diccionarios, títuloVentana, unidadMedida):
    limiteSuperior = __establecerLimiteSuperior(diccionarios)
    diccionarios = __establecerValores(diccionarios)
    plt.figure(títuloVentana, figsize=(9,0.9+0.15*limiteSuperior))
    for diccionario in diccionarios:
        color = diccionario['color']
        valoresx = diccionario['valoresx']
        valoresy = diccionario['valoresy']
        label = diccionario['nombre'] if len(diccionarios)>1 else ""
        plt.hlines(0,min(valoresx),max(valoresx), colors='k')
        plt.plot(valoresx, valoresy, 'o', color=color, label=label)
    if len(diccionarios)>1: plt.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    plt.xlabel(unidadMedida)
    plt.ylim(-1,limiteSuperior)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()

def __establecerValores(diccionarios):
    valsx = [val for dic in diccionarios for val in dic['muestra']]
    valsy = [valsx[0:i+1].count(valsx[i])-1 for i in range(len(valsx))]
    numElem = len(valsy)//len(diccionarios)
    listasy = [valsy[i:i+numElem] for i in range(0, len(valsy), numElem)]
    for diccionario, listay in zip(diccionarios,listasy):
        diccionario['valoresx'] = diccionario.pop('muestra')
        diccionario['valoresy'] = listay
    return diccionarios

def __establecerLimiteSuperior(diccionarios):
    valsx = [val for dic in diccionarios for val in dic['muestra']]
    return max([valsx.count(val) for val in valsx])