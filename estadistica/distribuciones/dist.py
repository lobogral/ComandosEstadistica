"""Ofrece una clase para manejo de distribuciones."""
from sympy import Piecewise
from sympy import piecewise_fold
from sympy import Rel
from sympy import Expr


class Dist():
    """Ofrece funciones para distribuciones.

    Attributes
    ----------
    func_dist
        Función de distribución

    Note
    ----
    De ahora en adelante las palabras función de distribución
    serán simplificadas como FD
    """

    func_dist: Expr = None

    def est_func_dist(self, func_dist: Expr) -> None:
        """Establece la FD.

        Parameters
        ----------
        func_dist
            Expresión de FD nueva
        """
        self.func_dist = func_dist

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
        func_troz = Piecewise((self.func_dist, rel), (0, True))
        func_troz_simpl = piecewise_fold(func_troz)
        return self.prob_total(func_troz_simpl)

    def prob_total(self,
                   func_dist_pru: Expr) -> Expr:
        """Calcula la probabilidad total de una FD.

        Parameters
        ----------
        func_dist_pru
            FD de prueba

        Returns
        -------
        Expr
            Expresión resultante sin Symbols
        """
