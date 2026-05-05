"""
Módulo de excepciones personalizadas del sistema.
"""

class ReservaError(Exception):
    """Error general en procesos de reserva."""
    pass

class ServicioNoDisponibleError(Exception):
    """Se lanza cuando un servicio no está disponible."""
    pass

class DatosInvalidosError(Exception):
    """Se lanza cuando hay datos incorrectos."""
    pass
