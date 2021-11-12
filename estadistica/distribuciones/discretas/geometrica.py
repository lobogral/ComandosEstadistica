"""Ofrece una clase para manejo de la distribución geometrica."""
from sympy import Piecewise
from sympy import Expr
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones.dist_conc import DistConc


class Geometrica(DistConc):
    """Ofrece funcionalidades para distribución geometrica."""

    def __init__(self,
                 var: Expr,
                 prob_exito: float) -> None:
        """Inicializa la clase.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        prob_exito
            Probabilidad de éxito
        """
        prob_fracaso = 1 - prob_exito
        func_dist = Piecewise((
            prob_exito*(prob_fracaso**(var-1)),
            var >= 1))
        self.dist = DistDisc()
        self.dist.est_func_dist(func_dist)
