"""Ofrece una clase para manejo de distribuciones."""
from sympy import Piecewise
from sympy import piecewise_fold
from sympy import Rel
from sympy import Expr


class Dist():
    """Ofrece funciones heredables para distribuciones.

    Attributes
    ----------
    func_dist
        Funcion de distribucion

    Note
    ----
    De ahora en adelante las palabras funcion de distribucion
    seran simplificadas como FD
    """

    func_dist: Expr = None

    def est_func_dist(self, func_dist: Expr) -> None:
        """Establece la FD.

        Parameters
        ----------
        func_dist
            Expresion de FD nueva
        """
        self.func_dist = func_dist

    def prob(self, relacion: Rel) -> Expr:
        """Calcula la probabilidad sobre una relacion de la FD.

        Parameters
        ----------
        relacion
            Relacion a la que se aplica el FD

        Returns
        -------
        Expr
            Expresion resultante sin Symbols
        """
        func_troz = Piecewise((self.func_dist, relacion), (0, True))
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
            Expresion resultante sin Symbols
        """
