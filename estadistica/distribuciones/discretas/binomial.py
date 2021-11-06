"""Ofrece una clase para manejo de la distribución binomial."""
from estadistica.distribuciones.dist_disc import DistDisc
from sympy import Piecewise
from sympy import Expr
from sympy import binomial as nC


class Binomial(DistDisc):
    """Ofrece funcionalidades para distribución binomial."""

    def __init__(self,
                 var: Expr,
                 prob_exito: float,
                 num_vals: int) -> None:
        """Constructor.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        num_vals
            Número de valores
        prob_exito
            Probabilidad de éxito
        """
        prob_fracaso = 1 - prob_exito
        func_dist = Piecewise((
            nC(num_vals, var)*(prob_exito**var)*(prob_fracaso**(num_vals-var)),
            (var >= 0) & (var <= num_vals)))
        self.est_func_dist(func_dist)
