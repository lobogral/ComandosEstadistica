from sympy import Piecewise, Symbol, solve, And
from sympy import Eq, piecewise_fold, simplify
from sympy import Naturals0, solveset, Intersection, Range
from sympy import FiniteSet, Contains, Rel, summation, oo
from itertools import product

dp = None

def establecerDp(dpNuevo):
    global dp
    dp = dpNuevo

def __AgregarIntervalo(función, area):
    funcionTrozos = Piecewise((función, area),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(dpPru, varsPru=None):
    if varsPru==None: varsPru=dpPru.atoms(Symbol)
    domPru = __EstablecerDominio(dpPru)
    prob = dpPru
    for var in varsPru:
        if isinstance(domPru[var], Range):
            inicio, final = domPru[var].args
            prob = summation(prob, (var,inicio, final - 1))
        else:
            vals = domPru[var]
            prob = sum([prob.subs(var, val) for val in vals])  
    return prob

def Prob(area):
    nuevaFunc = __AgregarIntervalo(dp, area)
    return ProbTotal(nuevaFunc)

def ProbMarginal(*varsMar):
    varsDp = dp.atoms(Symbol)
    varsMar = varsDp - {*varsMar}
    return simplify(ProbTotal(dp, varsMar))

def ProbCondicional(eqsDep, eqsIndep):
    valsIndep = solve(eqsIndep.atoms(Eq))
    varsIndep = eqsIndep.atoms(Symbol)
    funcCond = dp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(valsIndep))
    funcCondEvalEqs = __AgregarIntervalo(funcCondEval, eqsDep)
    return ProbTotal(funcCondEvalEqs)

def __EstablecerDominio(dp):
    eqs = dp.atoms(Eq)
    contains = dp.atoms(Contains)
    orders = dp.atoms(Rel) - eqs - contains
    dom = {}
    for var in dp.atoms(Symbol):
        dom[var] = [] if eqs or contains else Range(0,oo) 
    for eq in eqs:
        var, = eq.atoms(Symbol)
        val = solve(eq, var)
        dom[var] += val
    for contain in contains:
        var, = contain.atoms(Symbol)
        val = list(*contain.atoms(FiniteSet))
        dom[var] = val
    for order in orders:
        if eqs or contains: continue
        var, = order.atoms(Symbol)
        val = solveset(order, var, Naturals0)
        dom[var] = Intersection(dom[var], val)
    return dom

def dp2Dist(*vars):
    dom = __EstablecerDominio(dp)
    vals = [dom[var] for var in [*vars]]
    prodCart = list(product(*vals))
    return {k:dp.subs(dict(zip(vars,k))) for k in prodCart}

def dist2Dp(dist, vars):
    def genEq(tupl):
        return And(*[Eq(k, v) for k, v in zip(tupl, vars)])
    listaTrozDp = [(v, genEq(k)) for k, v in dist.items()]
    return Piecewise(*listaTrozDp)