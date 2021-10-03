from sympy import Piecewise, Symbol, solve, And
from sympy import Eq, piecewise_fold, simplify
from sympy import Integers, solveset, Range, EmptySet
from sympy import Rel, Sum
from itertools import product

dp = None

def establecer_dp(dp_nuevo):
    global dp
    dp = dp_nuevo

def __agregar_area(funcion, area):
    funcion_trozos = Piecewise((funcion, area),(0, True))
    return piecewise_fold(funcion_trozos)

def prob(area):
    nueva_funcion = __agregar_area(dp, area)
    return prob_total(nueva_funcion)

def prob_marginal(*vars_mar):
    vars_dp = dp.atoms(Symbol)
    vars_mar = vars_dp - {*vars_mar}
    prob = prob_total(dp, vars_mar)
    return simplify(prob)

def prob_condicional(area_dep, eqs_indep):
    vals_indep = solve(eqs_indep.atoms(Eq))
    vars_indep = eqs_indep.atoms(Symbol)
    func_cond = dp/prob_marginal(*vars_indep)
    func_cond_eval = simplify(func_cond.subs(vals_indep))
    func_cond_eval_area = __agregar_area(func_cond_eval, area_dep)
    return prob_total(func_cond_eval_area)

def prob_total(dp_pru, vars_pru=None):
    if vars_pru==None: vars_pru=dp_pru.atoms(Symbol)
    dom_pru = __establecer_dominio(dp_pru)
    prob = dp_pru
    for var in vars_pru:
        if isinstance(dom_pru[var], Range):
            inicio, final, _ = dom_pru[var].args
            prob = Sum(prob, (var, inicio, final - 1))
        else:
            vals = dom_pru[var]
            prob = sum([prob.subs(var, val) for val in vals])  
    return prob.doit()

def __establecer_dominio(dp):
    eqs = dp.atoms(Eq)
    orders = dp.atoms(Rel) - eqs
    dom = {var:EmptySet for var in dp.atoms(Symbol)} 
    for order in orders:
        if len(order.atoms(Symbol))>1: continue
        var, = order.atoms(Symbol)
        val = solveset(order, var, Integers)
        dom[var] = dom[var] & val if dom[var] else val
    for eq in eqs:
        var, = eq.atoms(Symbol)
        val = solveset(eq, var)
        dom[var] = dom[var] | val
    return dom

def dp_a_dist(*vars):
    dom = __establecer_dominio(dp)
    vals = [dom[var] for var in [*vars]]
    prod_cart = list(product(*vals))
    return {k:dp.subs(dict(zip(vars,k))) for k in prod_cart}

def dist_a_dp(dist, vars):
    def gen_eq(tupl):
        return And(*[Eq(k, v) for k, v in zip(tupl, vars)])
    lista_troz_dp = [(v, gen_eq(k)) for k, v in dist.items()]
    return Piecewise(*lista_troz_dp)