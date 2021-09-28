from sympy import Piecewise, Symbol, summation, piecewise_fold
from sympy import Rel, Range, solveset, Eq
from sympy import Integers, EmptySet

dp = None

def establecerDp(dpNuevo):
    global dp
    dp = dpNuevo

def __AgregarIntervalo(función, intervalo):
    funcionTrozos = Piecewise((función, intervalo),(0, True))
    return piecewise_fold(funcionTrozos)

def Prob(intervalo):
    nuevaFunc = __AgregarIntervalo(dp, intervalo)
    return ProbTotal(nuevaFunc)

def ProbTotal(dpPru):
    domPru = __EstablecerDominio(dpPru)
    var, = dpPru.atoms(Symbol)
    if isinstance(domPru[var], Range):
        inicio, final, _ = domPru[var].args
        return summation(dpPru, (var, inicio, final - 1))
    else:
        vals = domPru[var]
        return sum([dpPru.subs(var, val) for val in vals])

def ProbAcum():
    var, = dp.atoms(Symbol)
    dom = __EstablecerDominio(dp)
    vals = sorted(list(dom[var]))

    lista = []
    for i in range(len(vals)):
        subSuma = sum([dp.subs(var,val) for val in vals[:i]])
        llave = vals[i]
        lista += [(subSuma, (var<llave))]
    lista += [(1, True)]
    return Piecewise(*lista)

def __EstablecerDominio(dp):
    var, = dp.atoms(Symbol)
    eqs = dp.atoms(Eq)
    orders = dp.atoms(Rel) - eqs
    dom = {var:EmptySet}
    for order in orders:
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for eq in eqs:
        val = solveset(eq, var)
        dom[var] = dom[var] | val
    return dom

def dp2Dist():
    dom = __EstablecerDominio(dp)
    var, = dom.keys()
    vals = list(*dom.values())
    return {val:dp.subs({var: val}) for val in vals}

def dist2Dp(dist, var):
    listaTrozDp = [(v, Eq(var, k)) for k, v in dist.items()]
    return Piecewise(*listaTrozDp)