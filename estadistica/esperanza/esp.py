from math import prod
from math import sqrt
from sympy import Symbol
from sympy import Expr
from estadistica.distribuciones.dist import Dist


class Esp():

    dist: Dist = None

    def establecer_fdp(self, func_dist: Expr) -> None:
        """Establece la FD.

        Parameters
        ----------
        func_dist
            Expresion de FD nueva
        """
        self.dist.est_func_dist(func_dist)

    def esperanza(self, func):
        return self.dist.prob_total(func*self.dist.func_dist)

    def varianza(self, func):
        fdp = self.dist.func_dist
        return self.dist.prob_total(((func - self.esperanza(func))**2)*fdp)

    def varianza_alter(self, func):
        var, = func.atoms(Symbol)
        return self.esperanza(var**2) - self.esperanza(func)**2

    def desviacion(self, func):
        return sqrt(self.varianza(func))

    def covarianza(self):
        variables = self.dist.func_dist.atoms(Symbol)
        prod_var = prod(variables)
        prod_esp = prod([self.esperanza(var) for var in variables])
        return self.esperanza(prod_var)-prod_esp
