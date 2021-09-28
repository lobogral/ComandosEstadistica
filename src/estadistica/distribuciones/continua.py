from sympy import Piecewise, oo, simplify, integrate
from sympy import Symbol, piecewise_fold
from sympy.abc import t

fdp = None

def establecerFdp(fdpNuevo):
    global fdp
    fdp = fdpNuevo

def __AgregarIntervalo(función, intervalo):
    funcionTrozos = Piecewise((función, intervalo),(0, True))
    return piecewise_fold(funcionTrozos)

def Prob(intervalo):
    nuevaFunc = __AgregarIntervalo(fdp, intervalo)
    return ProbTotal(nuevaFunc)

def ProbTotal(fdpPru):
    varPru, = fdpPru.atoms(Symbol)
    return integrate(fdpPru, (varPru, -oo, oo))

def ProbAcum():
    var, = fdp.atoms(Symbol)
    integral = integrate(fdp.subs(var,t), (t, -oo, var))
    return simplify(integral.rewrite(Piecewise))