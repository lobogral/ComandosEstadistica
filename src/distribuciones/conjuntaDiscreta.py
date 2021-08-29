from sympy import Piecewise, Symbol, solve, And
from sympy import summation, Eq, piecewise_fold, simplify
from itertools import product

dp = None
dom = None

def establecerDpDom(dpNuevo, domNuevo):
    global dp
    global dom
    dp = dpNuevo
    dom = domNuevo

def __AgregarIntervalo(función, area):
    funcionTrozos = Piecewise((función, area),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(dpPru, domPru):
    prob = dpPru
    for var in domPru.keys():
        if isinstance(domPru[var], tuple):
            intervalo = (var, *domPru[var])
            prob = summation(prob, intervalo)
        else:
            vals = domPru[var]
            prob = sum([prob.subs(var, val) for val in vals])
    return prob

def Prob(area):
    nuevaFunc = __AgregarIntervalo(dp, area)
    return ProbTotal(nuevaFunc, dom)

def ProbMarginal(*varsMar):
    varsDp = dp.atoms(Symbol)
    domMar = {var:dom[var] for var in varsDp - {*varsMar}}
    return simplify(ProbTotal(dp, domMar))

def ProbCondicional(eqsDep, eqsIndep):
    valsDep = solve(eqsDep.atoms(Eq))
    valsIndep = solve(eqsIndep.atoms(Eq))
    varsIndep = eqsIndep.atoms(Symbol)
    funcCond = dp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(valsIndep))
    funcCondEvalEq = __AgregarIntervalo(funcCondEval, eqsDep)
    return simplify(funcCondEvalEq.subs(valsDep))

def dp2Dist():
    vars = dom.keys()
    vals = [dom[var] for var in vars]
    prodCart = list(product(*vals))
    return {k:dp.subs(dict(zip(vars,k))) for k in prodCart}

def dist2Dp(dist, vars):
    def genEq(tupl):
        return And(*[Eq(k, v) for k, v in zip(tupl, vars)])
    def genDomVar(dist, var):
        return list({val[vars.index(var)] for val in dist.keys()})
    listaTrozDp = [(v, genEq(k)) for k, v in dist.items()]
    listaDoms = {var: genDomVar(dist, var) for var in vars}
    return Piecewise(*listaTrozDp), listaDoms