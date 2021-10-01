from redondeo.redondeo import *

def __obtener_tabla(datos, paso, minimo, maximo, num_divisiones):
    tabla = []   
    div = (maximo-minimo)/num_divisiones
    for i in range(num_divisiones):
        min_cls = minimo + div*i
        max_cls = minimo + div*(i+1) - paso
        frec = len([dato for dato in datos if min_cls<=dato<=max_cls])
        tabla += [{
            'int_cls': f'{min_cls}-{max_cls}',
            'pnt_med': str((min_cls+max_cls)/2),
            'frec': frec,
            'frec_rel': redondear(frec/len(datos), 3)
        }]   
    return tabla

def imprimir_tabla(datos, paso, minimo, maximo, num_divisiones):
    tabla = __obtener_tabla(datos, paso, minimo, maximo, num_divisiones)
    str_int_cls = "Int. Cls.     "
    str_pnt_med = "Pnt. Med.    "
    str_frec = "Frec.    "
    str_frec_rel = "Frec. Rel."
    print(f'{str_int_cls}{str_pnt_med}{str_frec}{str_frec_rel}')
    for diccionario in tabla:
        int_cls = diccionario['int_cls']
        pnt_med = diccionario['pnt_med']
        frec = diccionario['frec']
        frec_rel = diccionario['frec_rel']
        print(int_cls, end="")
        espacios = len(str_int_cls) - len(int_cls) + len(str(pnt_med))
        print('{:>{}}'.format(pnt_med, espacios), end="")
        espacios = len(str_pnt_med) - len(str(pnt_med)) + len(str(frec))
        print('{:>{}}'.format(frec, espacios), end="")
        espacios = len(str_frec) - len(str(frec)) + len(str(frec_rel))
        print('{:>{}}'.format(frec_rel, espacios))

def establecer_datos_hist(datos, paso, minimo, maximo, num_divisiones):
    tabla = __obtener_tabla(datos, paso, minimo, maximo, num_divisiones)
    hist = {}
    hist['valores_x'] = [diccionario['pnt_med'] for diccionario in tabla]
    hist['valores_y'] = [diccionario['frec_rel'] for diccionario in tabla]
    return hist
