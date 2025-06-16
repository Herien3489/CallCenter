import csv
import json
import threading
import time
import random
from statistics import mean


class Agente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)
        self.estado = "activo"
        self.llamadas = []  # Lista para almacenar las llamadas realizadas por el agente

    def activar(self):
        self.estado = "activo"

    def desactivar(self):
        self.estado = "inactivo"

    def __str__(self):
        return f"Agente(nombre={self.nombre}, edad={self.edad}, estado={self.estado})"

    def __repr__(self):
        return self.__str__()

    # Leer desde archivo CSV
    @classmethod
    def cargar_desde_csv(cls, archivo_csv):
        agentes = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                agentes.append(cls(fila['nombre'], fila['edad']))
        return agentes

    # Leer desde archivo TXT (asumimos formato: nombre,edad por línea)
    @classmethod
    def cargar_desde_txt(cls, archivo_txt):
        agentes = []
        with open(archivo_txt, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    nombre, edad = partes
                    agentes.append(cls(nombre, edad))
        return agentes

    # Leer desde archivo JSON (asumimos lista de dicts con nombre y edad)
    @classmethod
    def cargar_desde_json(cls, archivo_json):
        agentes = []
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item in datos:
                agentes.append(cls(item['nombre'], item['edad']))
        return agentes
    def registrar_llamada(self, llamada):
        self.llamadas.append(llamada)

    def obtener_estadisticas(self):
        total = len(self.llamadas)
        exitosas = len([l for l in self.llamadas if l.exitosa])
        promedio_duracion = mean([l.duracion for l in self.llamadas]) if self.llamadas else 0
        return {
            'total': total,
            'exitosas': exitosas,
            'fallidas': total - exitosas,
            'efectividad': (exitosas / total) * 100 if total > 0 else 0,
            'promedio_duracion': promedio_duracion
        }

    def __str__(self):
        return f"{self.nombre} ({self.estado})"