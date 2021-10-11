from sympy import Piecewise, Symbol, summation, piecewise_fold
from sympy import Rel, Range, solveset, Eq
from sympy import Integers, EmptySet


dp = None


def establecer_dp(dp_nuevo):
    global dp
    dp = dp_nuevo


def __agregar_intervalo(funcion, intervalo):
    funcion_trozos = Piecewise((funcion, intervalo), (0, True))
    return piecewise_fold(funcion_trozos)


def prob(intervalo):
    nueva_func = __agregar_intervalo(dp, intervalo)
    return prob_total(nueva_func)


def prob_total(dp_pru):
    dom_pru = __establecer_dominio(dp_pru)
    var, = dp_pru.atoms(Symbol)
    if isinstance(dom_pru[var], Range):
        inicio, final, _ = dom_pru[var].args
        return summation(dp_pru, (var, inicio, final - 1))
    else:
        vals = dom_pru[var]
        return sum([dp_pru.subs(var, val) for val in vals])


def prob_acum():
    var, = dp.atoms(Symbol)
    dom = __establecer_dominio(dp)
    vals = sorted(list(dom[var]))

    lista = []
    for i in range(len(vals)):
        sub_suma = sum([dp.subs(var, val) for val in vals[:i]])
        llave = vals[i]
        lista += [(sub_suma, (var < llave))]
    lista += [(1, True)]
    return Piecewise(*lista)


def __establecer_dominio(dp):
    var, = dp.atoms(Symbol)
    eqs = dp.atoms(Eq)
    orders = dp.atoms(Rel) - eqs
    dom = {var: EmptySet}
    for order in orders:
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for eq in eqs:
        val = solveset(eq, var)
        dom[var] = dom[var] | val
    return dom


def dp_a_dist():
    dom = __establecer_dominio(dp)
    var, = dom.keys()
    vals = list(*dom.values())
    return {val: dp.subs({var: val}) for val in vals}


def dist_a_dp(dist, var):
    lista_troz_dp = [(v, Eq(var, k)) for k, v in dist.items()]
    return Piecewise(*lista_troz_dp)
