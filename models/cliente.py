from models.entidad import Entidad

class Cliente(Entidad):
    """
    Representa un cliente del sistema Software FJ.

    Aplica encapsulación para proteger los datos del usuario.
    """

    def __init__(self, nombre, email):
        """
        Inicializa un cliente con nombre y correo.

        Args:
            nombre (str): Nombre del cliente
            email (str): Correo electrónico
        """
        self.__nombre = None
        self.__email = None
        self.set_nombre(nombre)
        self.set_email(email)

    def set_nombre(self, nombre):
        """
        Valida y asigna el nombre del cliente.

        Args:
            nombre (str)

        Raises:
            ValueError: Si el nombre es inválido
        """
        if not nombre or len(nombre) < 3:
            raise ValueError("Nombre inválido")
        self.__nombre = nombre

    def set_email(self, email):
        """
        Valida y asigna el correo del cliente.

        Args:
            email (str)

        Raises:
            ValueError: Si el email es inválido
        """
        if "@" not in email:
            raise ValueError("Email inválido")
        self.__email = email

    def get_nombre(self):
        """Retorna el nombre del cliente."""
        return self.__nombre

    def get_email(self):
        """Retorna el correo del cliente."""
        return self.__email

    def mostrar_info(self):
        """
        Retorna información del cliente.

        Returns:
            str
        """
        return f"{self.__nombre} - {self.__email}"
