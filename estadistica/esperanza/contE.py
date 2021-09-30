from distribuciones import conjuntaContinua as conjCont
from sympy import Symbol
from math import prod

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
    vars = conjCont.fdp.atoms(Symbol)
    prodVars = prod(vars)
    prodEsp = prod([E(var) for var in vars])
    return E(prodVars)-prodEsp