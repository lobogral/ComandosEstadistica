from matplotlib import pyplot as plt

def dibujar(diccionarios, titulo_ventana, unidad_medida):
    limite_superior = __establecer_limite_superior(diccionarios)
    diccionarios = __establecer_valores(diccionarios)
    plt.figure(titulo_ventana, figsize=(9,0.9+0.15*limite_superior))
    for diccionario in diccionarios:
        color = diccionario['color']
        valores_x = diccionario['valores_x']
        valores_y = diccionario['valores_y']
        label = diccionario['nombre'] if len(diccionarios)>1 else ""
        plt.hlines(0,min(valores_x),max(valores_x), colors='k')
        plt.plot(valores_x, valores_y, 'o', color=color, label=label)
    if len(diccionarios)>1: plt.legend(bbox_to_anchor =(1.05, 1), loc='upper left')
    plt.xlabel(unidad_medida)
    plt.ylim(-1,limite_superior)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.tight_layout()
    plt.show()

def __establecer_valores(diccionarios):
    vals_x = [val for dic in diccionarios for val in dic['muestra']]
    vals_y = [vals_x[0:i+1].count(vals_x[i])-1 for i in range(len(vals_x))]
    num_elem = len(vals_y)//len(diccionarios)
    listas_y = [vals_y[i:i+num_elem] for i in range(0, len(vals_y), num_elem)]
    for diccionario, lista_y in zip(diccionarios,listas_y):
        diccionario['valores_x'] = diccionario.pop('muestra')
        diccionario['valores_y'] = lista_y
    return diccionarios

def __establecer_limite_superior(diccionarios):
    vals_x = [val for dic in diccionarios for val in dic['muestra']]
    return max([vals_x.count(val) for val in vals_x])