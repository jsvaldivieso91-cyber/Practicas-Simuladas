from abc import ABC, abstractmethod

class Entidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.

    Define la estructura mínima que deben implementar las clases derivadas.
    """

    @abstractmethod
    def mostrar_info(self):
        """
        Método abstracto que debe ser implementado por las clases hijas.

        Returns:
            str: Información representativa de la entidad
        """
        pass
