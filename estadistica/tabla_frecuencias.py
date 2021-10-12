"""Ofrece opciones para las tablas de frecuencias."""
from redondeo.redondeo import redondear


def imprimir_tabla(diccionario: dict) -> None:
    """Obtiene una tabla de frecuencias.

    Parameters
    ----------
    diccionario
        Diccionario que contiene lo siguiente
        {
            "muestra": muestra,
            "paso": paso,
            "minimo": minimo,
            "maximo": maximo,
            "num_div": num_div
        }

    """
    minimo = diccionario['minimo']
    maximo = diccionario['maximo']

    str_int_cls = "Int. Cls.     "
    str_pnt_med = "Pnt. Med.    "
    str_frec = "Frec.    "
    str_frec_rel = "Frec. Rel."
    print(f'{str_int_cls}{str_pnt_med}{str_frec}{str_frec_rel}')

    div = (maximo-minimo)/diccionario['num_div']
    for i in range(diccionario['num_div']):
        min_cls = minimo + div*i
        max_cls = minimo + div*(i+1) - diccionario['paso']

        int_cls = f'{min_cls}-{max_cls}'
        pnt_med = (min_cls+max_cls)/2
        frec = len([dato
                    for dato in diccionario['muestra']
                    if min_cls <= dato <= max_cls])

        frec_rel = redondear(frec/len(diccionario['muestra']), 3)
        print(f'{int_cls:{len(str_int_cls)}}', end="")
        print(f'{str(pnt_med):{len(str_pnt_med)}}', end="")
        print(f'{str(frec):{len(str_frec)}}', end="")
        print(frec_rel)
