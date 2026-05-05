"""
Módulo encargado del registro de eventos y errores del sistema.
"""

def registrar_log(mensaje):
    """
    Guarda un mensaje en el archivo logs.txt.

    Args:
        mensaje (str): Mensaje a registrar
    """
    with open("logs.txt", "a") as f:
        f.write(mensaje + "\n")
