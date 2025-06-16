import csv
import json

class Campaña:
    def __init__(self, nombre, producto, estado="activa"):
        self.nombre = nombre
        self.producto = producto
        self.estado = estado

    def activar(self):
        self.estado = "activa"

    def desactivar(self):
        self.estado = "inactiva"

    def __str__(self):
        return f"Campaña(nombre={self.nombre}, producto={self.producto}, estado={self.estado})"

    def __repr__(self):
        return self.__str__()

    # Leer desde archivo CSV
    @classmethod
    def cargar_desde_csv(cls, archivo_csv):
        campañas = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                campañas.append(cls(fila['nombre'], fila['producto'], fila.get('estado', 'activa')))
        return campañas

    # Leer desde archivo TXT (formato: nombre,producto[,estado])
    @classmethod
    def cargar_desde_txt(cls, archivo_txt):
        campañas = []
        with open(archivo_txt, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) >= 2:
                    nombre = partes[0]
                    producto = partes[1]
                    estado = partes[2] if len(partes) == 3 else "activa"
                    campañas.append(cls(nombre, producto, estado))
        return campañas

    # Leer desde archivo JSON (lista de dicts con nombre, producto, estado)
    @classmethod
    def cargar_desde_json(cls, archivo_json):
        campañas = []
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item in datos:
                campañas.append(cls(item['nombre'], item['producto'], item.get('estado', 'activa')))
        return campañas
