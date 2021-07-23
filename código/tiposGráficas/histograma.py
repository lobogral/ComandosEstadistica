import matplotlib.pyplot as plt

def dibujar(diccionarios, títuloVentana, unidadMedida):
    plt.figure(títuloVentana)
    plt.xlabel(unidadMedida)
    plt.ylabel("Probabilidad")
    valoresx = diccionarios['valoresx']
    valoresy = diccionarios['valoresy']
    plt.bar(valoresx, valoresy, width=1, edgecolor='black')
    plt.show()