"""Ofrece una clase para manejo de la distribución poisson."""
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones.dist_conc import DistConc
from sympy import Piecewise
from sympy import Expr
from sympy.functions import exp
from sympy.functions import factorial


class Poisson(DistConc):
    """Ofrece funcionalidades para distribución poisson."""

    def __init__(self,
                 var: Expr,
                 prom_inter: int) -> None:
        """Inicializa la clase.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        prom_inter
            Promedio en intervalo
        """
        func_dist = Piecewise((
            exp(-prom_inter)*(prom_inter**var)/factorial(var),
            var >= 0))
        self.dist = DistDisc()
        self.dist.est_func_dist(func_dist)
