from sympy import integrate, Piecewise, oo, solve
from sympy import simplify, piecewise_fold, Symbol, Eq

fdp = None

def establecerFdp(fdpNuevo):
    global fdp
    fdp = fdpNuevo

def __AgregarArea(función, area):
    funcionTrozos = Piecewise((función, area),(0, True))
    return piecewise_fold(funcionTrozos)

def Prob(area):
    nuevaFunc = __AgregarArea(fdp, area)
    return ProbTotal(nuevaFunc)

def ProbMarginal(*varsMar):
    varsFdp = fdp.atoms(Symbol)
    varsMar = varsFdp - {*varsMar}
    prob = ProbTotal(fdp, varsMar)
    return simplify(prob)

def ProbCondicional(areaDep, eqsIndep):
    valsIndep = solve(eqsIndep.atoms(Eq))
    varsIndep = eqsIndep.atoms(Symbol)
    funcCond = fdp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(valsIndep))
    funcCondEvalArea = __AgregarArea(funcCondEval, areaDep)
    return ProbTotal(funcCondEvalArea)

def ProbTotal(fdpPru, varsPru=None):
    if varsPru==None: varsPru=fdpPru.atoms(Symbol)
    lista = [(varPru, -oo, oo) for varPru in varsPru]
    prob = integrate(fdpPru, *lista)
    return piecewise_fold(prob.rewrite(Piecewise))
