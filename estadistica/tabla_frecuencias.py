from redondeo.redondeo import redondear


def __obtener_tabla(datos, paso, minimo, maximo, num_divisiones):

    """
    Obtiene los siguientes datos:
    - Intervalo de clase
    - Punto medio
    - Frecuencia
    - Frecuencia Relativa

    Parametros
    ----------
    datos: Arreglo de datos
    paso: Distancia minima entre un valor y otro
    minimo: Minimo valor admitido
    maximo: Maximo valor admitido
    num_divisiones: Numero de divisiones

    """

    tabla = []
    div = (maximo-minimo)/num_divisiones
    for i in range(num_divisiones):
        min_cls = minimo + div*i
        max_cls = minimo + div*(i+1) - paso
        frec = len([dato for dato in datos if min_cls <= dato <= max_cls])
        tabla += [{
            'int_cls': f'{min_cls}-{max_cls}',
            'pnt_med': str((min_cls+max_cls)/2),
            'frec': frec,
            'frec_rel': redondear(frec/len(datos), 3)
        }]
    return tabla


def imprimir_tabla(datos, paso, minimo, maximo, num_divisiones):

    """
    Imprime los siguientes datos:
    - Intervalo de clase
    - Punto medio
    - Frecuencia
    - Frecuencia Relativa

    Parametros
    ----------
    datos: Arreglo de datos
    paso: Distancia minima entre un valor y otro
    minimo: Minimo valor admitido
    maximo: Maximo valor admitido
    num_divisiones: Numero de divisiones

    """

    tabla = __obtener_tabla(datos, paso, minimo, maximo, num_divisiones)
    str_int_cls = "Int. Cls.     "
    str_pnt_med = "Pnt. Med.    "
    str_frec = "Frec.    "
    str_frec_rel = "Frec. Rel."

    print(f'{str_int_cls}{str_pnt_med}{str_frec}{str_frec_rel}')
    for diccionario in tabla:

        int_cls = diccionario['int_cls']
        pnt_med = diccionario['pnt_med']
        frec = str(diccionario['frec'])
        frec_rel = str(diccionario['frec_rel'])

        print(f'{int_cls:{len(str_int_cls)}}', end="")
        print(f'{pnt_med:{len(str_pnt_med)}}', end="")
        print(f'{frec:{len(str_frec)}}', end="")
        print(frec_rel)


def establecer_datos_hist(datos, paso, minimo, maximo, num_divisiones):

    """
    Cambia el formato para que se pueda graficar en un histograma:

    Parametros
    ----------
    datos: Arreglo de datos
    paso: Distancia minima entre un valor y otro
    minimo: Minimo valor admitido
    maximo: Maximo valor admitido
    num_divisiones: Numero de divisiones

    """

    tabla = __obtener_tabla(datos, paso, minimo, maximo, num_divisiones)
    hist = {}
    hist['valores_x'] = [diccionario['pnt_med'] for diccionario in tabla]
    hist['valores_y'] = [diccionario['frec_rel'] for diccionario in tabla]
    return hist
