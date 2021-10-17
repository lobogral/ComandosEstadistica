from math import prod
from math import sqrt
from sympy import Symbol
from sympy import Expr
from estadistica.distribuciones.dist import Dist


class Esp():

    dist: Dist = None

    def est_func_dist(self, func_dist: Expr) -> None:
        """Establece la FD.

        Parameters
        ----------
        func_dist
            Expresion de FD nueva
        """
        self.dist.est_func_dist(func_dist)

    def esperanza(self, var_alea):
        return self.dist.prob_total(var_alea*self.dist.func_dist)

    def varianza(self, var_alea):
        func_dist = self.dist.func_dist
        return self.dist.prob_total(
                   ((var_alea - self.esperanza(var_alea))**2)*func_dist)

    def varianza_alter(self, var_alea):
        var, = var_alea.atoms(Symbol)
        return self.esperanza(var**2) - self.esperanza(var_alea)**2

    def desviacion(self, var_alea):
        return sqrt(self.varianza(var_alea))

    def covarianza(self):
        variables = self.dist.func_dist.atoms(Symbol)
        prod_variables = prod(variables)
        prod_esperanzas = prod([self.esperanza(var) for var in variables])
        return self.esperanza(prod_variables)-prod_esperanzas
