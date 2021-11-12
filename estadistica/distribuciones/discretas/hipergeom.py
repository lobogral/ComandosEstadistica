"""Ofrece una clase para manejo de la distribución hipergeométrica."""
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones.dist_conc import DistConc
from sympy import Piecewise
from sympy import Expr
from sympy import binomial as nC


class Hipergeom(DistConc):
    """Ofrece funcionalidades para distribución hipergeométrica."""

    def __init__(self,
                 var: Expr,
                 num_vals: int,
                 muestra: int,
                 num_exi: int) -> None:
        """Inicializa la clase.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        num_vals
            Número de valores
        muestra
            Muestra del número de valores
        num_exi
            Número de exitos del número de valores
        """
        num_fra = num_vals - num_exi
        func_dist = Piecewise((
            (nC(num_exi, var)*nC(num_fra, muestra-var))/nC(num_vals, muestra),
            (var >= max(0, muestra-num_fra)) & (var <= min(muestra, num_exi))))
        self.dist = DistDisc()
        self.dist.est_func_dist(func_dist)
