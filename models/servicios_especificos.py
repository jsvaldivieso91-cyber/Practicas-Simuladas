from models.servicio import Servicio

class ReservaSala(Servicio):
    """
    Servicio de reserva de salas por horas.
    """

    def __init__(self, horas):
        super().__init__("Reserva Sala", 50000)
        if horas <= 0:
            raise ValueError("Horas inválidas")
        self.horas = horas

    def calcular_costo(self):
        """Calcula el costo total según las horas."""
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Sala por {self.horas} horas"


class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos por días.
    """

    def __init__(self, dias):
        super().__init__("Alquiler Equipo", 30000)
        if dias <= 0:
            raise ValueError("Días inválidos")
        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Equipo por {self.dias} días"


class Asesoria(Servicio):
    """
    Servicio de asesoría especializada.
    """

    def __init__(self, nivel):
        super().__init__("Asesoría", 80000)
        if nivel not in ["basico", "avanzado"]:
            raise ValueError("Nivel inválido")
        self.nivel = nivel

    def calcular_costo(self):
        """Aplica incremento si es asesoría avanzada."""
        return self.precio_base * (1.5 if self.nivel == "avanzado" else 1)

    def descripcion(self):
        return f"Asesoría {self.nivel}"
