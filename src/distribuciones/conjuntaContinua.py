from sympy import integrate, Piecewise, oo
from sympy import simplify, piecewise_fold, Symbol
from sympy.abc import x, y, z

def __AgregarIntervalo(función, intervalo):
    trozoImport = función.args[0]
    lista = [] 
    lista += [(trozoImport[0], trozoImport[1] & intervalo)]
    lista += [(0, True)]
    return Piecewise(*lista)

def ProbTotal(función):
    variables = función.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(función, *lista)

def Prob(función, intervalo):
    nuevaFunc = __AgregarIntervalo(simplify(función), intervalo)
    return ProbTotal(nuevaFunc)

def ProbMarginal(función, variable):
    variable = y if variable == x else x
    integral = integrate(función, (variable,-oo,oo))
    return simplify(piecewise_fold(integral.rewrite(Piecewise)))

def ProbCondicional(función, intervaloDep, varIndep, valIndep):
    varDep = y if varIndep == x else x
    funcCond = función/ProbMarginal(función, varIndep)
    funcCondEval = simplify(funcCond.subs(varIndep, valIndep))
    funcCondEvalInt = __AgregarIntervalo(funcCondEval, intervaloDep)
    return integrate(funcCondEvalInt, (varDep, -oo, oo))