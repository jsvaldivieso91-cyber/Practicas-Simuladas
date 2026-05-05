"""
Sistema principal Software FJ.

Este módulo ejecuta una simulación completa del sistema,
incluyendo creación de clientes, servicios, reservas y manejo de errores.
"""

from models.cliente import Cliente
from models.servicios_especificos import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from utils.logger import registrar_log


def main():
    """
    Función principal que ejecuta múltiples operaciones del sistema.
    """
    print("=== SOFTWARE FJ ===")

    operaciones = 0

    # CLIENTES
    try:
        c1 = Cliente("Juan Perez", "juan@mail.com")
        operaciones += 1
    except Exception as e:
        registrar_log(str(e))

    try:
        c2 = Cliente("An", "correo_mal")  # Error intencional
    except Exception as e:
        registrar_log(f"Cliente inválido: {str(e)}")

    # SERVICIOS
    try:
        s1 = ReservaSala(2)
        s2 = AlquilerEquipo(3)
        s3 = Asesoria("avanzado")
        operaciones += 3
    except Exception as e:
        registrar_log(str(e))

    # RESERVAS
    try:
        r1 = Reserva(c1, s1)
        print(r1.confirmar())

        r2 = Reserva(c1, s2)
        print(r2.confirmar())

        r3 = Reserva(c1, s3)
        print(r3.confirmar())

        operaciones += 3

    except Exception as e:
        registrar_log(str(e))

    finally:
        print("\nSistema funcionando correctamente")
        print(f"Operaciones realizadas: {operaciones}")


if __name__ == "__main__":
    main()
