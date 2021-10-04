from estadistica.distribuciones import conjunta_discreta as conj_disc
from estadistica.distribuciones import discreta as disc
from math import prod, sqrt
from sympy import Symbol

establecer_dp = conj_disc.establecer_dp

def E(func):
    dp = conj_disc.dp
    return conj_disc.prob_total(func*dp)

def Var(func):
    dp = conj_disc.dp
    return conj_disc.prob_total(((func - E(func))**2)*dp)

def Var_Alter(func):
    var, = func.atoms(Symbol)
    return E(var**2) - E(func)**2

def desv(func):
    return sqrt(Var(func))

def Cov():
    vars = conj_disc.dp.atoms(Symbol)
    prod_Var = prod(vars)
    prod_E = prod([E(var) for var in vars])
    return E(prod_Var)-prod_E

def dist_a_dp(dist, vars):
    if(isinstance(vars, Symbol)):
        return disc.dist_a_dp(dist, vars)
    else:
        return conj_disc.dist_a_dp(dist, vars)

