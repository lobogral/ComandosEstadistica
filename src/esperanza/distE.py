from distribuciones import conjuntaDiscreta as conjDisc
from distribuciones import discreta as disc
from functools import reduce
from sympy import Symbol
from math import sqrt

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
    dp = conjDisc.dp
    mulSymbol = reduce(lambda a, b: a*b, dp.atoms(Symbol))
    mulEsp = reduce(lambda a, b: E(a)*E(b), dp.atoms(Symbol))
    return E(mulSymbol)-mulEsp

def dist2Dp(dist, vars):
    if(isinstance(vars, Symbol)):
        return disc.dist2Dp(dist, vars)
    else:
        return conjDisc.dist2Dp(dist, vars)

