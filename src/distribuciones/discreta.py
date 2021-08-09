from sympy import Piecewise
from sympy.abc import x

def Func2Dist(función, variable, valores):
    return {valor:función.subs(variable, valor) for valor in valores}

def ProbTotal(distribución):
    dicc = distribución
    return sum([v for k,v in dicc.items()])

def ProbAcum(distribución):
    dicc = distribución
    lista = []
    for i in range(len(dicc)):
        subSuma = sum([v for k,v in dicc.items()][:i])
        llave = [k for k,v in dicc.items()][i]
        lista += [(subSuma, (x<llave))]
    lista += [(1, True)]
    return Piecewise(*lista)