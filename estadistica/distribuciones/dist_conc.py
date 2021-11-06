"""Ofrece una clase para manejo de la distribución concreta."""
from sympy import Expr
from sympy import Rel
from estadistica.distribuciones.dist import Dist


class DistConc():
    """Ofrece funcionalidades para distribución uniforme.

    Attributes
    ----------
    dist
        Función de distribución
    """

    dist: Dist

    def prob(self, rel: Rel) -> Expr:
        """Calcula la probabilidad sobre una relación de la FD.

        Parameters
        ----------
        rel
            Relación a la que se aplica el FD

        Returns
        -------
        Expr
            Expresión resultante sin Symbols
        """
        return self.dist.prob(rel)

    def ret_dist(self) -> Dist:
        """Retorna la distribución de probabilidad.

        Returns
        -------
        Dist
            Distribución de probabilidad
        """
        return self.dist
