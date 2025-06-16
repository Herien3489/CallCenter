import csv
import json

class Cliente:
    def __init__(self, nombre, telefono, no_llamar=False):
        self.nombre = nombre
        self.telefono = telefono
        self.no_llamar = no_llamar  # Booleano que indica si pidió no ser contactado

    def marcar_no_llamar(self):
        self.no_llamar = True

    def __str__(self):
        return f"Cliente(nombre={self.nombre}, telefono={self.telefono}, no_llamar={self.no_llamar})"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def cargar_desde_csv(cls, archivo_csv):
        clientes = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                no_llamar = fila.get('no_llamar', 'False').lower() in ['true', '1', 'yes']
                clientes.append(cls(fila['nombre'], fila['telefono'], no_llamar))
        return clientes

    @classmethod
    def cargar_desde_txt(cls, archivo_txt):
        clientes = []
        with open(archivo_txt, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) >= 2:
                    nombre, telefono = partes[:2]
                    no_llamar = len(partes) > 2 and partes[2].lower() in ['true', '1', 'yes']
                    clientes.append(cls(nombre, telefono, no_llamar))
        return clientes

    @classmethod
    def cargar_desde_json(cls, archivo_json):
        clientes = []
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item in datos:
                clientes.append(cls(
                    item['nombre'],
                    item['telefono'],
                    item.get('no_llamar', False)
                ))
        return clientes
