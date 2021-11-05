"""Comandos para esperanza continua."""
from estadistica.distribuciones.dist_conj_cont import DistConjCont
from estadistica.esperanza.esp import Esp


class EspCont(Esp):
    """Ofrece funciones de esperanza continua."""

    def __init__(self):
        """Inicializa la clase."""
        super().__init__(DistConjCont())
