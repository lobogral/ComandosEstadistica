from sympy import integrate, Piecewise, oo, solve
from sympy import simplify, piecewise_fold, Symbol, Eq

fdp = None

def establecer_fdp(fdp_nuevo):
    global fdp
    fdp = fdp_nuevo

def __agregar_area(funcion, area):
    funcion_trozos = Piecewise((funcion, area),(0, True))
    return piecewise_fold(funcion_trozos)

def prob(area):
    nueva_funcion = __agregar_area(fdp, area)
    return prob_total(nueva_funcion)

def prob_marginal(*vars_mar):
    vars_fdp = fdp.atoms(Symbol)
    vars_mar = vars_fdp - {*vars_mar}
    prob = prob_total(fdp, vars_mar)
    return simplify(prob)

def prob_condicional(area_dep, eqs_indep):
    vals_indep = solve(eqs_indep.atoms(Eq))
    vars_indep = eqs_indep.atoms(Symbol)
    func_cond = fdp/prob_marginal(*vars_indep)
    func_cond_eval = simplify(func_cond.subs(vals_indep))
    func_cond_eval_area = __agregar_area(func_cond_eval, area_dep)
    return prob_total(func_cond_eval_area)

def prob_total(fdp_pru, vars_pru=None):
    if vars_pru==None: vars_pru=fdp_pru.atoms(Symbol)
    lista = [(var_pru, -oo, oo) for var_pru in vars_pru]
    prob = integrate(fdp_pru, *lista)
    return piecewise_fold(prob.rewrite(Piecewise))
