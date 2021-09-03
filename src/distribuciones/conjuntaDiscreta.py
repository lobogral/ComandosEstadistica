from sympy import Piecewise, Symbol, solve, And
from sympy import Eq, piecewise_fold, simplify
from sympy import Naturals0, solveset, Range, EmptySet
from sympy import FiniteSet, Contains, Rel, Sum, oo
from itertools import product

dp = None

def establecerDp(dpNuevo):
    global dp
    dp = dpNuevo

def __AgregarArea(función, area):
    funcionTrozos = Piecewise((función, area),(0, True))
    return piecewise_fold(funcionTrozos)

def Prob(area):
    nuevaFunc = __AgregarArea(dp, area)
    return ProbTotal(nuevaFunc)

def ProbMarginal(*varsMar):
    varsDp = dp.atoms(Symbol)
    varsMar = varsDp - {*varsMar}
    prob = ProbTotal(dp, varsMar)
    return simplify(prob)

def ProbCondicional(eqsDep, eqsIndep):
    valsIndep = solve(eqsIndep.atoms(Eq))
    varsIndep = eqsIndep.atoms(Symbol)
    funcCond = dp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(valsIndep))
    funcCondEvalEqs = __AgregarArea(funcCondEval, eqsDep)
    return ProbTotal(funcCondEvalEqs)

def ProbTotal(dpPru, varsPru=None):
    if varsPru==None: varsPru=dpPru.atoms(Symbol)
    domPru = __EstablecerDominio(dpPru)
    prob = dpPru
    for var in varsPru:
        if isinstance(domPru[var], Range):
            inicio, final, _ = domPru[var].args
            prob = Sum(prob, (var, inicio, final - 1))
        else:
            vals = domPru[var]
            prob = sum([prob.subs(var, val) for val in vals])  
    return prob.doit()

def __EstablecerDominio(dp):
    eqs = dp.atoms(Eq)
    contains = dp.atoms(Contains)
    orders = dp.atoms(Rel) - eqs
    dom = {var:EmptySet for var in dp.atoms(Symbol)} 
    for order in orders:
        if len(order.atoms(Symbol))>1: continue
        var, = order.atoms(Symbol)
        val = solveset(order, var, Naturals0)
        dom[var] = dom[var] & val if dom[var] else val
    for eq in eqs:
        var, = eq.atoms(Symbol)
        val = solveset(eq, var)
        dom[var] = dom[var] | val
    for contain in contains:
        var, = contain.atoms(Symbol)
        val, = contain.atoms(FiniteSet)
        dom[var] = dom[var] | val
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