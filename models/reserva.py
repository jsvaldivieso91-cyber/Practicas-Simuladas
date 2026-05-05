from datetime import datetime
from exceptions.custom_exceptions import ReservaError
from utils.logger import registrar_log

class Reserva:
    def __init__(self, cliente, servicio):
        if cliente is None or servicio is None:
            raise ValueError("Cliente o servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"
        self.fecha = datetime.now()

    def confirmar(self):
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
        self.estado = "cancelada"
        return "Reserva cancelada"
