"""Comandos para distribuciones conjuntas continuas."""
from sympy import Symbol
from sympy import Range
from sympy import Sum
from sympy import Expr
from estadistica.distribuciones.dist_conj import DistConj
from estadistica.transf.transf_conj import establecer_dominio


class DistConjDisc(DistConj):
    """Ofrece funciones para distribuciones conjuntas discretas."""

    def prob_total_var(self,
                       func_dist_pru: Expr,
                       vars_pru: set[Symbol]) -> Expr:
        """Calcula la probabilidad total por variable de una FD.

        Para mas información revisar
        docstring de la clase padre (DistConj)
        """
        dom_pru = establecer_dominio(func_dist_pru)
        prob = func_dist_pru
        for var in vars_pru:
            if isinstance(dom_pru[var], Range):
                inicio, final, _ = dom_pru[var].args
                prob = Sum(prob, (var, inicio, final - 1))
            else:
                vals = dom_pru[var]
                prob = sum([prob.subs(var, val) for val in vals])
        return prob.doit()
