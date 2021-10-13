"""Comandos para una distribucion continua.

La distibucion continua tambien es llamada
funcion de densidad de probabilidad (fdp)
"""
from sympy import Piecewise
from sympy import oo
from sympy import simplify
from sympy import integrate
from sympy import Symbol
from sympy import piecewise_fold
from sympy import Rel
from sympy import Expr
from sympy.abc import t


FDP: Expr = None


def establecer_fdp(fdp_nuevo: Expr) -> None:
    """Establece la FDP.

    Parameters
    ----------
    fdp_nuevo
        Expresion de densidad nueva
    """
    global FDP
    FDP = fdp_nuevo


def prob(relacion: Rel) -> Expr:
    """Calcula la probabilidad sobre una relacion de la FDP.

    Parameters
    ----------
    relacion
        Relacion a la que se aplica el FDP

    Returns
    -------
    Expr
        Expresion resultante sin Symbols
    """
    func_troz = Piecewise((FDP, relacion), (0, True))
    func_troz_simpl = piecewise_fold(func_troz)
    return prob_total(func_troz_simpl)


def prob_total(fdp_pru: Expr) -> Expr:
    """Calcula la probabilidad total de una fdp.

    Parameters
    ----------
    fdp_pru
        Fdp de prueba

    Returns
    -------
    Expr
        Expresion resultante sin Symbols
    """
    var_pru, = fdp_pru.atoms(Symbol)
    return integrate(fdp_pru, (var_pru, -oo, oo))


def prob_acum() -> Piecewise:
    """Calcula la probabilidad acumulada de la FDP.

    Returns
    -------
    Piecewise
        Funcion a trozos resultante
    """
    var, = FDP.atoms(Symbol)
    integral = integrate(FDP.subs(var, t), (t, -oo, var))
    return simplify(integral.rewrite(Piecewise))
