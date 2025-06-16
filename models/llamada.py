import threading
import time
import random
from statistics import mean

class Llamada:
    def __init__(self, agente, duracion, exitosa, observacion=""):
        self.agente = agente
        self.duracion = duracion  # segundos
        self.exitosa = exitosa
        self.observacion = observacion
    def simular_llamada(agente, lock):
        print(f"Iniciando llamada para {agente.nombre}...")
    
        duracion = random.randint(3, 8)  # segundos simulados
        time.sleep(duracion)
    
        exitosa = random.choice([True, False])
        observacion = "Cliente interesado" if exitosa else "Cliente colgó"
    
        llamada = Llamada(agente, duracion, exitosa, observacion)
    
        with lock:  # asegurar acceso seguro
            agente.registrar_llamada(llamada)
            print(f"Finalizó llamada ({'✔' if exitosa else '✘'}) de {duracion}s para {agente.nombre}")
