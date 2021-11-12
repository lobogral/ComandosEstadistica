"""Ofrece una clase para manejo de la distribución binomial negativa."""
from sympy import Piecewise
from sympy import Expr
from sympy import binomial as nC
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones.dist_conc import DistConc


class BinNeg(DistConc):
    """Ofrece funcionalidades para distribución binomial negativa."""

    def __init__(self,
                 var: Expr,
                 prob_exito: float,
                 k_exito: int) -> None:
        """Inicializa la clase.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        k_exito
            k-ésimo éxito
        prob_exito
            Probabilidad de éxito
        """
        prob_fracaso = 1 - prob_exito
        comb = nC(var-1, k_exito-1)
        func_dist = Piecewise((
            comb*(prob_exito**k_exito)*(prob_fracaso**(var-k_exito)),
            var >= k_exito))
        self.dist = DistDisc()
        self.dist.est_func_dist(func_dist)
