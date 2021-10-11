from sympy import Piecewise, oo, simplify, integrate
from sympy import Symbol, piecewise_fold
from sympy.abc import t


fdp = None


def establecer_fdp(fdp_nuevo):
    global fdp
    fdp = fdp_nuevo


def __agregar_intervalo(funcion, intervalo):
    funcion_trozos = Piecewise((funcion, intervalo), (0, True))
    return piecewise_fold(funcion_trozos)


def prob(intervalo):
    nueva_func = __agregar_intervalo(fdp, intervalo)
    return prob_total(nueva_func)


def prob_total(fdp_pru):
    var_pru, = fdp_pru.atoms(Symbol)
    return integrate(fdp_pru, (var_pru, -oo, oo))


def prob_acum():
    var, = fdp.atoms(Symbol)
    integral = integrate(fdp.subs(var, t), (t, -oo, var))
    return simplify(integral.rewrite(Piecewise))
