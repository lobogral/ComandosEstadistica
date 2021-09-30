from distribuciones import conjuntaDiscreta as conjDisc
from distribuciones import discreta as disc
from math import prod, sqrt
from sympy import Symbol

establecerDp = conjDisc.establecerDp

def E(func):
    dp = conjDisc.dp
    return conjDisc.ProbTotal(func*dp)

def Var(func):
    dp = conjDisc.dp
    return conjDisc.ProbTotal(((func - E(func))**2)*dp)

def VarAlter(func):
    var, = func.atoms(Symbol)
    return E(var**2) - E(func)**2

def desv(func):
    return sqrt(Var(func))

def Cov():
    vars = conjDisc.dp.atoms(Symbol)
    prodVars = prod(vars)
    prodEsp = prod([E(var) for var in vars])
    return E(prodVars)-prodEsp

def dist2Dp(dist, vars):
    if(isinstance(vars, Symbol)):
        return disc.dist2Dp(dist, vars)
    else:
        return conjDisc.dist2Dp(dist, vars)

