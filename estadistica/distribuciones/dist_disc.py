"""Comandos para una distribución discreta."""
from sympy import Piecewise
from sympy import Symbol
from sympy import summation
from sympy import Range
from sympy import Expr
from estadistica.distribuciones.dist import Dist
from estadistica.distribuciones.transf import establecer_dominio


class DistDisc(Dist):
    """Ofrece funciones para distribuciones discretas."""

    def prob_total(self,
                   func_dist_pru: Expr) -> Expr:
        """Calcula la probabilidad total de una FD.

        Para mas información revisar
        docstring de la clase padre (Dist)
        """
        dom_pru = establecer_dominio(func_dist_pru)
        var, = func_dist_pru.atoms(Symbol)
        if isinstance(dom_pru[var], Range):
            inicio, final, _ = dom_pru[var].args
            return summation(func_dist_pru, (var, inicio, final - 1))
        vals = dom_pru[var]
        return sum([func_dist_pru.subs(var, val) for val in vals])

    def prob_acum(self) -> Piecewise:
        """Calcula la probabilidad acumulada de la FD.

        Returns
        -------
        Piecewise
            Función a trozos resultante
        """
        var, = self.func_dist.atoms(Symbol)
        dom = establecer_dominio(self.func_dist)
        vals = sorted(list(dom[var]))

        lista = []
        for i, _ in enumerate(vals):
            sub_suma = sum([self.func_dist.subs(var, val) for val in vals[:i]])
            llave = vals[i]
            lista += [(sub_suma, (var < llave))]
        lista += [(1, True)]
        return Piecewise(*lista)
