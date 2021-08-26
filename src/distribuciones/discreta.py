from sympy import Piecewise, Symbol, summation, Eq

def Func2Troz(dp, dom):
    var, = dp.atoms(Symbol)
    lista = [(dp.subs(var,val), Eq(var,val)) for val in dom[var]]
    return Piecewise(*lista)

def ProbTotal(dpPru, domPru):
    var, = dpPru.atoms(Symbol)
    if isinstance(domPru[var], tuple):
        intervalo = (var, *domPru[var])
        return summation(dpPru, intervalo)
    else:
        vals = domPru[var]
        return sum([dpPru.subs(var, val) for val in vals])

def ProbAcum(dp, dom):
    var, = dp.atoms(Symbol)
    if isinstance(dom[var], tuple):
        vals = range(*[sum(arr) for arr in zip(dom[var], (0,1))])
    else:
        vals = dom[var]

    lista = []
    for i in range(len(dp.args)):
        subSuma = sum([dp.subs(var,val) for val in vals[:i]])
        llave = vals[i]
        lista += [(subSuma, (var<llave))]
    lista += [(1, True)]
    return Piecewise(*lista)