"""Ofrece funcionalidades para conteo de puntos muestrales."""
from math import prod


def factorial(num: int) -> int:
    """Calcula el factorial de un numero.

    Parameters
    ----------
    num
        Numero al que se le calcula el factorial

    Returns
    -------
    int
        Factorial

    """
    return num * factorial(num-1) if num > 1 else 1


def perms(num_elems: int, num_selec: int) -> int:
    """Calcula permutaciones.

    Calcula el numero de permutaciones de los elementos
    de un conjunto tomados una cantidad de elementos
    a la vez.

    Parameters
    ----------
    num_elems
        Numero de elementos de un conjunto
    num_selec
        Numero de elementos seleccionados a la vez

    Return
    ------
    int
        Numero de permutaciones

    """
    return factorial(num_elems) // factorial(num_elems-num_selec)


def perms_clase(num_elems: int, list_num_selec: list[int]) -> int:
    """Calcula permutaciones de clase.

    Calcula el numero de permutaciones de clase de los
    elementos de un conjunto tomados en una lista
    de grupos de elementos.

    Parameters
    ----------
    num_elems
        Numero de elementos de un conjunto
    list_num_select
        Lista de grupos de elementos

    Return
    ------
    int
        Numero de permutaciones de clase

    """
    mult = prod([factorial(i) for i in list_num_selec])
    return factorial(num_elems) // mult


def combs(num_elems: int, num_selec: int) -> int:
    """Calcula combinaciones.

    Calcula el numero de combinaciones de los elementos
    de un conjunto tomados una cantidad de elementos
    a la vez.

    Parameters
    ----------
    num_elems
        Numero de elementos de un conjunto
    num_selec
        Numero de elementos seleccionados a la vez

    Return
    ------
    int
        Numero de combinaciones

    """
    return perms_clase(num_elems, [num_selec, num_elems-num_selec])
