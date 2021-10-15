"""Ofrece funcionalidades de transformacion."""
from sympy import Piecewise
from sympy import Symbol
from sympy import Rel
from sympy import solveset
from sympy import Eq
from sympy import Integers
from sympy import EmptySet
from sympy import Expr


def establecer_dominio(func_dist: Expr) -> dict:
    """Establece el dominio a partir de una FD.

    Parameters
    ----------
    func_dist
        Distribucion de probabilidad

    Returns
    -------
    dict
        Dominio
    """
    var, = func_dist.atoms(Symbol)
    equations = func_dist.atoms(Eq)
    orders = func_dist.atoms(Rel) - equations
    dom = {var: EmptySet}
    for order in orders:
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for equation in equations:
        val = solveset(equation, var)
        dom[var] = dom[var] | val
    return dom


def dp_a_dist(func_dist: Expr) -> dict:
    """Transforma la expresion FD a un diccionario.

    Parameters
    ----------
    func_dist
        Funcion de distribucion

    Returns
    -------
    dict
        Distribucion en forma de diccionario

    """
    dom = establecer_dominio(func_dist)
    var, = dom.keys()
    vals: list = list(*dom.values())
    return {val: func_dist.subs({var: val}) for val in vals}


def dist_a_dp(dist: dict,
              var: Symbol) -> Expr:
    """Transforma un diccionario (dist) a una expresion (FD).

    Parameters
    ----------
    dist
        Diccionario de distribucion de probabilidad
    var
        Variable

    Returns
    -------
    Expr
        Distribucion en forma de expresion
    """
    lista_troz_dp = [(v, Eq(var, k)) for k, v in dist.items()]
    return Piecewise(*lista_troz_dp)
