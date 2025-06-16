import csv
import json
from abc import ABC, abstractmethod
from statistics import mean

# Clase base abstracta
class Agente(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = int(edad)
        self.estado = "activo"
        self.llamadas = []

    def activar(self):
        self.estado = "activo"

    def desactivar(self):
        self.estado = "inactivo"

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

    @classmethod
    def cargar_desde_csv(cls, archivo_csv):
        agentes = []
        with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                agentes.append(AgenteJunior(fila['nombre'], fila['edad']))
        return agentes

    @classmethod
    def cargar_desde_txt(cls, archivo_txt):
        agentes = []
        with open(archivo_txt, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    nombre, edad = partes
                    agentes.append(AgenteJunior(nombre, edad))
        return agentes

    @classmethod
    def cargar_desde_json(cls, archivo_json):
        agentes = []
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            for item in datos:
                agentes.append(AgenteJunior(item['nombre'], item['edad']))
        return agentes

    def __str__(self):
        return f"{self.nombre} ({self.estado})"

    @abstractmethod
    def obtener_tipo(self):
        pass


class AgenteJunior(Agente):
    def obtener_tipo(self):
        return "Junior"


class AgenteSenior(Agente):
    def obtener_tipo(self):
        return "Senior"
