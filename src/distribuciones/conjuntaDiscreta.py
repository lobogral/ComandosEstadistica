from sympy import Piecewise, Symbol, solve, And
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

def ProbMarginal(*varMar):
    def selec(vals):
        lista = [vals[vars.index(var)] for var in vars if var in [*varMar]]
        return lista.pop() if (len([*varMar])==1) else tuple(lista)
    def suma(val):
        return sum([v for k,v in dist.items() if selec(k) == val])
    listaVar = list(set([selec(k) for k,v in dist.items()]))
    return {var:suma(var) for var in listaVar}

def ProbCondicional(listEqDep, listEqIndep):
    def resolver(listEqs, varsSelec):
        lista = [solve(listEqs)[var] for var in vars if var in varsSelec]
        return lista.pop() if (len(varsSelec)==1) else tuple(lista)
    varsIndep = And(*listEqIndep).atoms(Symbol)
    valsIndep = resolver(listEqIndep, varsIndep)
    vals = resolver(listEqDep + listEqIndep, vars)
    marginal = ProbMarginal(*varsIndep)
    return dist[vals]/marginal[valsIndep]