"""Comandos para distribuciones conjuntas continuas."""
from sympy import integrate
from sympy import Piecewise
from sympy import oo
from sympy import piecewise_fold
from sympy import Symbol
from sympy import Expr
from estadistica.distribuciones.dist_conj import DistConj


class DistConjCont(DistConj):
    """Ofrece funciones para distribuciones conjuntas continuas."""

    def prob_total(self,
                   func_dist_pru: Expr,
                   vars_pru: set[Symbol] = None) -> Expr:
        """Calcula la probabilidad total de una FD.

        Para mas informacion revisar
        docstring de la clase abuela (Dist)
        """
        if vars_pru is None:
            vars_pru = func_dist_pru.atoms(Symbol)
        lista = [(var_pru, -oo, oo) for var_pru in vars_pru]
        prob = integrate(func_dist_pru, *lista)
        return piecewise_fold(prob.rewrite(Piecewise))
