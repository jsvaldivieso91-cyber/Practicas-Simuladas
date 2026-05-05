from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general del sistema.
    """

    def __init__(self, nombre, precio_base):
        """
        Inicializa el servicio.

        Args:
            nombre (str): Nombre del servicio
            precio_base (float): Precio base del servicio
        """
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        """
        Calcula el costo del servicio.

        Returns:
            float
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Retorna la descripción del servicio.

        Returns:
            str
        """
        pass
