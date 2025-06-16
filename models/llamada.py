class Llamada:
    def __init__(self, agente, duracion, exitosa, observacion=""):
        self.agente = agente
        self.duracion = duracion  # segundos
        self.exitosa = exitosa
        self.observacion = observacion

    def __str__(self):
        estado = "Éxito" if self.exitosa else "Fallo"
        return f"Llamada de {self.duracion}s - {estado}: {self.observacion}"
