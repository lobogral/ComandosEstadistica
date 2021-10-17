"""Comandos para esperanza discreta."""
from estadistica.esperanza.esp import Esp
from estadistica.distribuciones.dist_conj_disc import DistConjDisc


class EspDisc(Esp):
    """Ofrece funciones de esperanza discreta."""

    def __init__(self):
        """Inicializa la clase."""
        self.dist = DistConjDisc()
