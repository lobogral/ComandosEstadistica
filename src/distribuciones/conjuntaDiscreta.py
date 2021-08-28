from sympy import Piecewise, Symbol, solve, And
from sympy import summation, Eq, piecewise_fold, simplify
from itertools import product

dp = None
dom = None

def establecerDpDom(dpNuevo, domNuevo=None):
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

def Func2Troz():
    vars = dom.keys()
    vals = [dom[var] for var in vars]
    prodCart = list(product(*vals))
    return {k:dp.subs(dict(zip(vars,k))) for k in prodCart}

def Prob(area):
    restric = __AgregarIntervalo(dp, area)
    return ProbTotal(restric, dom)

def ProbMarginal(*varsMar):
    varsDp = dp.atoms(Symbol)
    domMar = {var:dom[var] for var in varsDp - {*varsMar}}
    return simplify(ProbTotal(dp, domMar))

def ProbCondicional(listEqDep, listEqIndep):
    valsDep = solve(listEqDep, dict=True)
    valsIndep = solve(listEqIndep, dict=True)
    varsIndep = And(*listEqIndep).atoms(Symbol)
    funcCond = dp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(*valsIndep))
    funcCondEvalEq = __AgregarIntervalo(funcCondEval, And(*listEqDep))
    return simplify(funcCondEvalEq.subs(*valsDep))