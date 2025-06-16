import threading
import random
import time
from models.llamada import Llamada

def simular_llamada(agente, lock):
    print(f"\n Iniciando llamada para {agente.nombre}...")
    duracion = random.randint(3, 8)
    time.sleep(duracion)
    exitosa = random.choice([True, False])
    observacion = "Cliente interesado" if exitosa else "Cliente colgó"

    llamada = Llamada(agente, duracion, exitosa, observacion)

    with lock:
        agente.registrar_llamada(llamada)
        print(f"✅ Finalizó llamada de {duracion}s para {agente.nombre} ({'✔' if exitosa else '✘'})")

def ejecutar_llamadas_concurrentes(agentes):
    lock = threading.Lock()
    hilos = []

    for agente in agentes:
        hilo = threading.Thread(target=simular_llamada, args=(agente, lock))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
