from sympy import integrate, Piecewise, oo, simplify
from sympy.abc import t

def ÁreaBajoCurva(función, variable):
    return integrate(función, (variable,-oo,oo))

def Prob(función, variable, a, b):
    return integrate(función,(variable,a,b))

def ProbAcum(función, variable, valor=None):
    if valor==None:
        integral = integrate(función.subs(variable,t), (t, -oo, variable))
        return simplify(integral.rewrite(Piecewise))
    else:
        return integrate(función, (variable, -oo, valor))