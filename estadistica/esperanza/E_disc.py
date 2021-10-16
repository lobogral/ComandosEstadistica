from estadistica.distribuciones.dist_conj_disc import DistConjDisc
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones import transf
from estadistica.distribuciones import transf_conj
from math import prod, sqrt
from sympy import Symbol


dist_disc = DistDisc()
dist_conj_disc = DistConjDisc()
establecer_dp = dist_conj_disc.est_func_dist


def E(func):
    dp = dist_conj_disc.func_dist
    return dist_conj_disc.prob_total(func*dp)


def Var(func):
    dp = dist_conj_disc.func_dist
    return dist_conj_disc.prob_total(((func - E(func))**2)*dp)


def Var_Alter(func):
    var, = func.atoms(Symbol)
    return E(var**2) - E(func)**2


def desv(func):
    return sqrt(Var(func))


def Cov():
    vars = dist_conj_disc.func_dist.atoms(Symbol)
    prod_Var = prod(vars)
    prod_E = prod([E(var) for var in vars])
    return E(prod_Var)-prod_E


def dist_a_dp(dist, vars):
    if(isinstance(vars, Symbol)):
        return transf.dist_a_dp(dist, vars)
    else:
        return transf_conj.dist_a_dp(dist, vars)
