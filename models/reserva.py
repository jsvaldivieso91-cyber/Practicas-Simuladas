from datetime import datetime
from utils.logger import registrar_log
from exceptions.custom_exceptions import ReservaError

class Reserva:
    """
    Representa una reserva en el sistema.
    """

    def __init__(self, cliente, servicio):
        """
        Inicializa una reserva.

        Args:
            cliente (Cliente)
            servicio (Servicio)
        """
        if cliente is None or servicio is None:
            raise ValueError("Cliente o servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"
        self.fecha = datetime.now()

    def confirmar(self):
        """
        Confirma la reserva calculando el costo.

        Returns:
            str
        """
        try:
            costo = self.servicio.calcular_costo()
        except Exception as e:
            registrar_log(f"Error cálculo: {str(e)}")
            raise ReservaError("Error en cálculo") from e
        else:
            self.estado = "confirmada"
            return f"Confirmada - Total: {costo}"
        finally:
            registrar_log("Intento de confirmación ejecutado")

    def cancelar(self):
        """
        Cancela la reserva.

        Returns:
            str
        """
        self.estado = "cancelada"
        return "Reserva cancelada"
