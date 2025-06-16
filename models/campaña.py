class Campania:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.llamadas = []  

    def agregar_llamada(self, llamada):
        self.llamadas.append(llamada)

    def __str__(self):
        return f"Campaña(nombre={self.nombre}, descripcion={self.descripcion})"
