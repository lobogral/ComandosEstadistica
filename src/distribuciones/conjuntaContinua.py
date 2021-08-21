from sympy import integrate, Piecewise, oo
from sympy import simplify, piecewise_fold, Symbol

x = Symbol("x", real=True)
y = Symbol("y", real=True)

fdp = x

def establecerFdp(fdpNuevo):
    global fdp
    fdp = fdpNuevo

def __AgregarIntervalo(función, intervalo):
    funcionTrozos = Piecewise((función, intervalo),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(fdpPrueba):
    variables = fdpPrueba.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(fdpPrueba, *lista)

def Prob(intervalo):
    nuevaFunc = __AgregarIntervalo(fdp, intervalo)
    return ProbTotal(nuevaFunc)

def ProbMarginal(variable):
    variable = y if variable == x else x
    integral = integrate(fdp, (variable,-oo,oo))
    return simplify(piecewise_fold(integral.rewrite(Piecewise)))

def ProbCondicional(intervaloDep, eqDep):
    varIndep = eqDep.args[0]
    valIndep = eqDep.args[1]
    varDep = y if varIndep == x else x
    funcCond = fdp/ProbMarginal(varIndep)
    funcCondEval = simplify(funcCond.subs(varIndep, valIndep))
    funcCondEvalInt = __AgregarIntervalo(funcCondEval, intervaloDep)
    return integrate(funcCondEvalInt, (varDep, -oo, oo))