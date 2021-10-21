"""Ofrece funcionalidades de transformacion.

Esta enfocado principalmente en
distribuciones discretas conjuntas

"""
from itertools import product
from sympy import Piecewise
from sympy import Symbol
from sympy import Eq
from sympy import Rel
from sympy import solveset
from sympy import Integers
from sympy import EmptySet
from sympy import Expr
from sympy import And


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
    equations = func_dist.atoms(Eq)
    orders = func_dist.atoms(Rel) - equations
    dom = {var: EmptySet for var in func_dist.atoms(Symbol)}
    for order in orders:
        if len(order.atoms(Symbol)) > 1:
            continue
        var, = order.atoms(Symbol)
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for equation in equations:
        var, = equation.atoms(Symbol)
        val = solveset(equation, var)
        dom[var] = dom[var] | val
    return dom


def dp_a_dist(func_dist: Expr,
              *variables: Symbol) -> dict:
    """Transforma la expresion FD a un diccionario.

    Parameters
    ----------
    func_dist
        Funcion de distribucion
    *variables
        Variables ordenadas

    Returns
    -------
    dict
        Distribucion en forma de diccionario

    Note
    ----
    La distribucion se presenta de acuerdo al orden
    de como se ingresan las *variables

    """
    dom = establecer_dominio(func_dist)
    vals = [dom[var] for var in [*variables]]
    prod_cart = list(product(*vals))
    return {k: func_dist.subs(dict(zip(variables, k))) for k in prod_cart}


def dist_a_dp(dist: dict,
              variables: list[Symbol]) -> Expr:
    """Transforma un diccionario (dist) a una expresion (FD).

    Parameters
    ----------
    dist
        Diccionario de distribucion de probabilidad
    variables
        Lista de variables

    Returns
    -------
    Expr
        Distribucion en forma de expresion
    """
    def gen_eq(tupl):
        return And(*[Eq(k, v) for k, v in zip(tupl, variables)])
    lista_troz_func_dist = [(v, gen_eq(k)) for k, v in dist.items()]
    return Piecewise(*lista_troz_func_dist)
