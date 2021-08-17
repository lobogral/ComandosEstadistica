from sympy import Piecewise, Symbol

x = Symbol("x", real=True)
y = Symbol("y", real=True)

def Func2Dist(función, valoresX, valoresY):
    return {
        (valX, valY):función.subs({x:valX, y:valY}) 
        for valX in valoresX for valY in valoresY
    }

def ProbTotal(distribución):
    dicc = distribución
    return sum([v for k,v in dicc.items()])

def Prob(distribución, área):
    dicc = distribución
    return sum(
        [v for (valx,valy),v in dicc.items() 
        if área.subs({x:valx, y:valy})]
    )

def ProbMarginal(distribución, variable):
    dicc = distribución
    num = 0 if variable == x else 1
    listaVar = list(set([k[num] for k,v in dicc.items()]))
    suma = lambda val : sum([v for k,v in dicc.items() if k[num] == val])
    return {var:suma(var) for var in listaVar}


def ProbCondicional(distribución, varDep, valX, valY):
    valDep = valX if varDep == x else valY
    marginal = ProbMarginal(distribución, varDep)
    return distribución[(valX, valY)]/marginal[valDep]