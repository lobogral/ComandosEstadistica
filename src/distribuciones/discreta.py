from sympy import Piecewise, Symbol, summation, Eq, piecewise_fold
from sympy import Contains, Rel, Range, oo, solveset
from sympy import Naturals0, Intersection, FiniteSet, solve

dp = None

def establecerDp(dpNuevo):
    global dp
    dp = dpNuevo

def __AgregarIntervalo(función, intervalo):
    funcionTrozos = Piecewise((función, intervalo),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(dpPru):
    domPru = __EstablecerDominio(dpPru)
    var, = dpPru.atoms(Symbol)
    if isinstance(domPru[var], Range):
        inicio, final, _ = domPru[var].args
        return summation(dpPru, (var, inicio, final - 1))
    else:
        vals = domPru[var]
        return sum([dpPru.subs(var, val) for val in vals])

def Prob(intervalo):
    nuevaFunc = __AgregarIntervalo(dp, intervalo)
    return ProbTotal(nuevaFunc)

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
    contains = dp.atoms(Contains)
    orders = dp.atoms(Rel) - eqs - contains
    dom = {var:[]} if eqs or contains else {var:Range(0,oo)}
    for eq in eqs:
        val = solve(eq, var)
        dom[var] += val
    for contain in contains:
        val = list(*contain.atoms(FiniteSet))
        dom[var] = val
    for order in orders:
        if eqs or contains: continue
        val = solveset(order, var, Naturals0)
        dom[var] = Intersection(dom[var], val)
    return dom

def dp2Dist():
    dom = __EstablecerDominio(dp)
    var, = dom.keys()
    vals = list(*dom.values())
    return {val:dp.subs({var: val}) for val in vals}

def dist2Dp(dist, var):
    listaTrozDp = [(v, Eq(var, k)) for k, v in dist.items()]
    return Piecewise(*listaTrozDp)