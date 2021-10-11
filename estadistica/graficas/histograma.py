import matplotlib.pyplot as plt


def dibujar(diccionarios, titulo_ventana, unidad_medida):
    plt.figure(titulo_ventana)
    plt.xlabel(unidad_medida)
    plt.ylabel("Probabilidad")
    valores_x = diccionarios['valores_x']
    valores_y = diccionarios['valores_y']
    plt.bar(valores_x, valores_y, width=1, edgecolor='black')
    plt.show()
