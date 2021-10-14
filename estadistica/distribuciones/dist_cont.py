"""Comandos para una distribucion continua."""
from sympy import Piecewise
from sympy import oo
from sympy import simplify
from sympy import integrate
from sympy import Symbol
from sympy import Expr
from sympy.abc import t
from estadistica.distribuciones.dist import Dist


class DistCont(Dist):
    """Ofrece funciones para distribuciones continuas."""

    def prob_total(self, func_dist_pru: Expr) -> Expr:
        """Calcula la probabilidad total de una FD.

        Para mas informacion revisar
        docstring de la clase padre (Dist)
        """
        var_pru, = func_dist_pru.atoms(Symbol)
        return integrate(func_dist_pru, (var_pru, -oo, oo))

    def prob_acum(self) -> Piecewise:
        """Calcula la probabilidad acumulada de la FD.

        Returns
        -------
        Piecewise
            Funcion a trozos resultante
        """
        var, = self.func_dist.atoms(Symbol)
        integral = integrate(self.func_dist.subs(var, t), (t, -oo, var))
        return simplify(integral.rewrite(Piecewise))
