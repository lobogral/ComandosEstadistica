"""Ofrece una clase para manejo de la esperanza matemática.

Esto incluye tanto la definición de la esperanza como sus
derivados, por ejemplo la varianza, la desviación estándar,
y la covarianza.
"""
from math import prod
from math import sqrt
from sympy import Symbol
from sympy import Expr
from estadistica.distribuciones.dist import Dist


class Esp():
    """Ofrece funciones para esperanza matemática.

    Attributes
    ----------
    dist
        Función de distribución

    """

    dist: Dist

    def est_func_dist(self, func_dist: Expr) -> None:
        """Establece la FD.

        Parameters
        ----------
        func_dist
            Expresión de FD nueva
        """
        self.dist.est_func_dist(func_dist)

    def esperanza(self, var_alea: Expr) -> Expr:
        """Calcula la esperanza matemática.

        Parameters
        ----------
        var_alea
            Variable aleatoria

        Returns
        -------
        Expr
            Esperanza matemática
        """
        return self.dist.prob_total(var_alea*self.dist.func_dist)

    def varianza(self, var_alea: Expr) -> Expr:
        """Calcula la varianza.

        Parameters
        ----------
        var_alea
            Variable aleatoria

        Returns
        -------
        Expr
            Varianza
        """
        func_dist = self.dist.func_dist
        return self.dist.prob_total(
                   ((var_alea - self.esperanza(var_alea))**2)*func_dist)

    def varianza_alter(self, var_alea: Expr) -> Expr:
        """Ofrece una alternativa para calcular la varianza.

        Parameters
        ----------
        var_alea
            Variable aleatoria

        Returns
        -------
        Expr
            Varianza

        Note
        ----
        Se debe anotar que el método solo funciona
        para una variable
        """
        var, = var_alea.atoms(Symbol)
        return self.esperanza(var**2) - self.esperanza(var_alea)**2

    def desviacion(self, var_alea: Expr) -> Expr:
        """Calcula la desviación estándar.

        Parameters
        ----------
        var_alea
            Variable aleatoria

        Returns
        -------
        Expr
            Desviación estándar
        """
        return sqrt(self.varianza(var_alea))

    def covarianza(self) -> Expr:
        """Calcula la covarianza.

        Returns
        -------
        Expr
            Covarianza
        """
        variables = self.dist.func_dist.atoms(Symbol)
        prod_variables = prod(variables)
        prod_esperanzas = prod([self.esperanza(var) for var in variables])
        return self.esperanza(prod_variables)-prod_esperanzas
