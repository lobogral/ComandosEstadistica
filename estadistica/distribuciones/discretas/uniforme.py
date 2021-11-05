"""Ofrece una clase para manejo de la distribución uniforme."""
from fractions import Fraction
from estadistica.distribuciones.dist_disc import DistDisc
from sympy import Piecewise
from sympy import Expr


class Uniforme(DistDisc):
    """Ofrece funcionalidades para distribución uniforme."""

    def est_vals_dist(self,
                      num_vals: int,
                      inter_vals: Expr) -> None:
        """Establece valores para distribución.

        Establece valores concretos para que se pueda
        crear la distribución y con ello establecer
        dicha distribución.

        Parameters
        ----------
        num_vals
            Número de valores
        inter_vals
            Intervalo o conjunto de valores
        """
        func_dist = Piecewise((Fraction(1, num_vals), inter_vals))
        self.est_func_dist(func_dist)
