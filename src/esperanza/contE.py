from distribuciones import conjuntaContinua as conjCont
from functools import reduce
from sympy import Symbol

establecerFdp = conjCont.establecerFdp

def E(func):
    return conjCont.ProbTotal(func*conjCont.fdp)

def Var(func):
    fdp = conjCont.fdp
    return conjCont.ProbTotal(((func - E(func))**2)*fdp)

def VarAlter(func):
    var, = func.atoms(Symbol)
    return E(var**2) - E(func)**2

def desv(func):
    return sqrt(Var(func))

def Cov():
    fdp = conjCont.fdp
    mulSymbol = reduce(lambda a, b: a*b, fdp.atoms(Symbol))
    mulEsp = reduce(lambda a, b: E(a)*E(b), fdp.atoms(Symbol))
    return E(mulSymbol)-mulEsp