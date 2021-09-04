from distribuciones import conjuntaDiscreta as conjDisc
from distribuciones import discreta as disc
from sympy import Symbol

establecerDp = conjDisc.establecerDp

def E(func):
    return conjDisc.ProbTotal(func*conjDisc.dp)

def dist2Dp(dist, vars):
    if(isinstance(vars, Symbol)):
        return disc.dist2Dp(dist, vars)
    else:
        return conjDisc.dist2Dp(dist, vars)

