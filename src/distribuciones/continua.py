from sympy import Piecewise, oo, simplify, integrate, Symbol
from sympy.stats import P, cdf

Prob = P

def ProbTotal(fdp):
    variable = fdp.atoms(Symbol)
    return integrate(fdp, (variable,-oo,oo))

def ProbAcum(continuaVA):
    variable = continuaVA.atoms(Symbol)
    integral = cdf(continuaVA)(*variable)
    return simplify(integral.rewrite(Piecewise))