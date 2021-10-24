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

    def prob_total_var(self,
                       func_dist_pru: Expr,
                       vars_pru: set[Symbol]) -> Expr:
        """Calcula la probabilidad total por variable de una FD.

        Para mas información revisar
        docstring de la clase padre (DistConj)
        """
        lista = [(var_pru, -oo, oo) for var_pru in vars_pru]
        prob = integrate(func_dist_pru, *lista)
        return piecewise_fold(prob.rewrite(Piecewise))
