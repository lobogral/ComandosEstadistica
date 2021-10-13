"""Comandos para una distribucion discreta (dp)."""
from sympy import Piecewise
from sympy import Symbol
from sympy import summation
from sympy import piecewise_fold
from sympy import Rel
from sympy import Range
from sympy import solveset
from sympy import Eq
from sympy import Integers
from sympy import EmptySet
from sympy import Expr


DP: Expr = None


def establecer_dp(dp_nuevo: Expr) -> None:
    """Establece la DP.

    Parameters
    ----------
    dp_nuevo
        Expresion de distribucion nueva
    """
    global DP
    DP = dp_nuevo


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
    """Calcula la probabilidad sobre una relacion de la DP.

    Parameters
    ----------
    relacion
        Relacion a la que se aplica el DP

    Returns
    -------
    Expr
        Expresion resultante sin Symbols
    """
    nueva_func = __agregar_relacion(DP, relacion)
    return prob_total(nueva_func)


def prob_total(dp_pru):
    """Calcula la probabilidad total de una dp.

    Parameters
    ----------
    dp_pru
        Dp de prueba

    Returns
    -------
    Expr
        Expresion resultante sin Symbols
    """
    dom_pru = __establecer_dominio(dp_pru)
    var, = dp_pru.atoms(Symbol)
    if isinstance(dom_pru[var], Range):
        inicio, final, _ = dom_pru[var].args
        return summation(dp_pru, (var, inicio, final - 1))
    vals = dom_pru[var]
    return sum([dp_pru.subs(var, val) for val in vals])


def prob_acum() -> Piecewise:
    """Calcula la probabilidad acumulada de la DP.

    Returns
    -------
    Piecewise
        Funcion a trozos resultante
    """
    var, = DP.atoms(Symbol)
    dom = __establecer_dominio(DP)
    vals = sorted(list(dom[var]))

    lista = []
    for i, _ in enumerate(vals):
        sub_suma = sum([DP.subs(var, val) for val in vals[:i]])
        llave = vals[i]
        lista += [(sub_suma, (var < llave))]
    lista += [(1, True)]
    return Piecewise(*lista)


def __establecer_dominio(dist_prob: Expr) -> dict:
    """Establece el dominio a partir de una dp.

    Parameters
    ----------
    dist_prob
        Distribucion de probabilidad

    Returns
    -------
    dict
        Dominio
    """
    var, = dist_prob.atoms(Symbol)
    equations = dist_prob.atoms(Eq)
    orders = dist_prob.atoms(Rel) - equations
    dom = {var: EmptySet}
    for order in orders:
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for equation in equations:
        val = solveset(equation, var)
        dom[var] = dom[var] | val
    return dom


def dp_a_dist() -> dict:
    """Transforma la expresion DP a un diccionario.

    Returns
    -------
    dict
        Distribucion en forma de diccionario
    """
    dom = __establecer_dominio(DP)
    var, = dom.keys()
    vals: list = list(*dom.values())
    return {val: DP.subs({var: val}) for val in vals}


def dist_a_dp(dist: dict,
              var: Symbol) -> Expr:
    """Transforma un diccionario (dist) a una expresion (dp).

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
