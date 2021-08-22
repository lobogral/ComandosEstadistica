from sympy import integrate, Piecewise, oo, solve, And
from sympy import simplify, piecewise_fold, Symbol

fdp = None

def establecerFdp(fdpNuevo):
    global fdp
    fdp = fdpNuevo

def __AgregarIntervalo(función, area):
    funcionTrozos = Piecewise((función, area),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(fdpPrueba):
    variables = fdpPrueba.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(fdpPrueba, *lista)

def Prob(area):
    nuevaFunc = __AgregarIntervalo(fdp, area)
    return ProbTotal(nuevaFunc)

def ProbMarginal(*variablesMar):
    variablesFdp = fdp.atoms(Symbol)
    lista = [
        (variable, -oo, oo) 
        for variable in variablesFdp - {*variablesMar}
    ]
    integral = integrate(fdp, *lista) if lista else fdp
    return simplify(piecewise_fold(integral.rewrite(Piecewise)))

def ProbCondicional(areaDep, *eqsIndep):
    varsIndep = And(*eqsIndep).atoms(Symbol)
    valsIndep = solve([*eqsIndep], dict=True)
    funcCond = fdp/ProbMarginal(*varsIndep)
    funcCondEval = simplify(funcCond.subs(*valsIndep))
    funcCondEvalArea = __AgregarIntervalo(funcCondEval, areaDep)
    return ProbTotal(funcCondEvalArea)