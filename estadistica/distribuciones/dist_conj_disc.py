"""Comandos para distribuciones conjuntas continuas."""
from sympy import Symbol
from sympy import Range
from sympy import Sum
from sympy import Expr
from estadistica.distribuciones.dist_conj import DistConj
from estadistica.distribuciones.transf_conj import establecer_dominio


class DistConjDisc(DistConj):
    """Ofrece funciones para distribuciones conjuntas discretas."""

    def prob_total(self,
                   func_dist_pru: Expr,
                   vars_pru: set[Symbol] = None) -> Expr:
        """Calcula la probabilidad total de una FD.

        Para mas informacion revisar
        docstring de la clase abuela (Dist)
        """
        if vars_pru is None:
            vars_pru = func_dist_pru.atoms(Symbol)
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
