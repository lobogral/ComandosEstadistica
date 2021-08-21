from sympy import Piecewise, oo, simplify, integrate
from sympy.stats import P, cdf

Prob = P

def ProbTotal(fdp, variable):
    return integrate(fdp, (variable,-oo,oo))

def ProbAcum(continuaVA, variable):
    integral = cdf(continuaVA)(variable)
    return simplify(integral.rewrite(Piecewise))