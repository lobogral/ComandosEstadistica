"""Comandos para una distribuciones conjuntas."""
from sympy import Piecewise
from sympy import solve
from sympy import simplify
from sympy import piecewise_fold
from sympy import Symbol
from sympy import Eq
from sympy import Expr
from estadistica.distribuciones.dist import Dist


class DistConj(Dist):
    """Ofrece funciones heredables para distribuciones conjuntas."""

    def prob_marginal(self, *vars_mar: Symbol) -> Expr:
        """Calcula la probabilidad marginal.

        Parameters
        ----------
        *vars_mar
            Variables marginales
        """
        vars_fdp = self.func_dist.atoms(Symbol)
        vars_mar = vars_fdp - {*vars_mar}
        prob = self.prob_total(self.func_dist, vars_mar)
        return simplify(prob)

    def prob_condicional(self,
                         area_dep: Expr,
                         eqs_indep: Expr) -> Expr:
        """Calcula la probabilidad condicional.

        Parameters
        ----------
        area_dep
            Area de dependencia
        eqs_indep
            Ecuaciones de independencia
        """
        vals_indep = solve(eqs_indep.atoms(Eq))
        vars_indep = eqs_indep.atoms(Symbol)
        func_cond = self.func_dist/self.prob_marginal(*vars_indep)
        func_cond_eval = simplify(func_cond.subs(vals_indep))
        func_cond_eval_area = piecewise_fold(
            Piecewise(
                (func_cond_eval, area_dep),
                (0, True)))
        return self.prob_total(func_cond_eval_area)
