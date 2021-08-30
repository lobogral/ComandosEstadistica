from sympy import Piecewise, Symbol, solve, And, Contains, FiniteSet
from sympy import summation, Eq, piecewise_fold, simplify, oo
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
        if domPru[var]:
            vals = domPru[var]
            prob = sum([prob.subs(var, val) for val in vals])
        else:
            prob = summation(prob, (var,0,oo))
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
    dom = {var:[] for var in dp.atoms(Symbol)}
    for eq in dp.atoms(Eq):
        var, = eq.atoms(Symbol)
        val = solve(eq, var)
        dom[var] += val
    for contain in dp.atoms(Contains):
        var, = contain.atoms(Symbol)
        val = list(*contain.atoms(FiniteSet))
        dom[var] = val
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