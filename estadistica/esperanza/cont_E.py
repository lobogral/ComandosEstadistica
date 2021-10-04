from estadistica.distribuciones import conjunta_continua as conj_cont
from sympy import Symbol
from math import prod

establecer_fdp = conj_cont.establecer_fdp

def E(func):
    return conj_cont.prob_total(func*conj_cont.fdp)

def Var(func):
    fdp = conj_cont.fdp
    return conj_cont.prob_total(((func - E(func))**2)*fdp)

def Var_Alter(func):
    var, = func.atoms(Symbol)
    return E(var**2) - E(func)**2

def desv(func):
    return sqrt(Var(func))

def Cov():
    vars = conj_cont.fdp.atoms(Symbol)
    prod_Var = prod(vars)
    prod_E = prod([E(var) for var in vars])
    return E(prod_Var)-prod_E