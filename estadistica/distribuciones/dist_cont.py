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
    """Establece el FDP.

    Parameters
    ----------
    fdp_nuevo
        Expresion de densidad nueva
    """
    global FDP
    FDP = fdp_nuevo


def __agregar_relacion(expresion: Expr,
                       relacion: Rel) -> Piecewise:
    """Crea una funcion a trozos con la relacion.

    La intencion es crear una nueva expresion (Piecewise),
    en la cual la expresion actual es valida en la relacion
    planteada y fuera de esta la nueva expresion es 0.

    Parameters
    ----------
    expresion
        Expresion actual
    relacion
        Relacion a la que se aplica la expresion

    Returns
    -------
    Piecewise
        Nueva expresion (Funcion a trozos resultante)
    """
    funcion_trozos = Piecewise((expresion, relacion), (0, True))
    return piecewise_fold(funcion_trozos)


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
    nueva_func = __agregar_relacion(FDP, relacion)
    return prob_total(nueva_func)


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
