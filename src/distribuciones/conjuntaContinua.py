from sympy import integrate, Piecewise, oo, simplify, piecewise_fold
from sympy.abc import t, x, y

def Prob(función, intervalo):
    trozoImport = función.args[0]
    lista = [] 
    lista += [(trozoImport[0], trozoImport[1] & intervalo)]
    lista += [(0, True)]
    nuevaFunc = Piecewise(*lista)
    return integrate(nuevaFunc, (x, -oo, oo), (y, -oo, oo))

def ProbMarginal(función, variable):
    variable = y if variable == x else x
    integral = integrate(función, (variable,-oo,oo))
    return simplify(piecewise_fold(integral.rewrite(Piecewise)))

def ProbCondicional(función, valDep1, valDep2, varIndep, valIndep):
    varDep = y if varIndep == x else x
    funcCond = función/ProbMarginal(función, varIndep)
    funcCondEval = funcCond.subs(varIndep, valIndep)
    return integrate(funcCondEval, (varDep, valDep1, valDep2))
