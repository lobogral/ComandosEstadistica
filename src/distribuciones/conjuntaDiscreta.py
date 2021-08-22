from sympy import Piecewise, Symbol, solve
from itertools import product

dist = None
vars = None

def establecerDist(distNueva, varsNuevas):
    global dist
    global vars
    dist = distNueva
    vars = varsNuevas

def Func2Dist(función, vars, *vals):
    return {
        k:función.subs(dict(zip(vars,k))) 
        for k in list(product(*vals))
    }

def ProbTotal(distPrueba):
    dicc = distPrueba
    return sum([v for k,v in dicc.items()])

def Prob(área):
    dicc = dist
    return sum(
        [v for k,v in dicc.items() 
        if área.subs(dict(zip(vars,k)))]
    )

def ProbMarginal(varMar):
    dicc = dist
    num = vars.index(varMar)
    listaVar = list(set([k[num] for k,v in dicc.items()]))
    suma = lambda val : sum([v for k,v in dicc.items() if k[num] == val])
    return {var:suma(var) for var in listaVar}


def ProbCondicional(eqDep, eqIndep):
    varIndep, = eqIndep.atoms(Symbol)
    valIndep, = solve(eqIndep)
    vals = tuple([solve([eqDep, eqIndep])[var] for var in vars])
    marginal = ProbMarginal(varIndep)
    return dist[vals]/marginal[valIndep]