import threading
import random
import time
from models.llamada import Llamada
from models.cliente import Cliente

# Suponemos que esta lista se pasa desde afuera o se carga antes
clientes = []

def simular_llamada(agente, lock, pila=None):
    if not clientes:
        print("⚠️ No hay clientes cargados.")
        return

    cliente = random.choice(clientes)

    if cliente.no_llamar:
        print(f"⛔ Cliente {cliente.nombre} pidió no ser contactado. Saltando llamada.")
        return

    if pila is not None:
        pila.append(f"Inicia llamada con {agente.nombre} a {cliente.nombre}")

    print(f"\n📞 Iniciando llamada para {agente.nombre} a cliente {cliente.nombre}...")
    duracion = random.randint(3, 8)
    time.sleep(duracion)
    exitosa = random.choice([True, False])
    observacion = "Cliente interesado" if exitosa else "Cliente colgó"

    llamada = Llamada(agente, duracion, exitosa, observacion)

    with lock:
        agente.registrar_llamada(llamada)
        print(f"✅ Finalizó llamada de {duracion}s a {cliente.nombre} ({'✔' if exitosa else '✘'})")

    if pila is not None:
        pila.append(f"Finaliza llamada con {agente.nombre} a {cliente.nombre}")

def ejecutar_llamadas_concurrentes(agentes, lista_clientes):
    global clientes
    clientes = lista_clientes

    lock = threading.Lock()
    hilos = []
    pila = []

    for agente in agentes:
        hilo = threading.Thread(target=simular_llamada, args=(agente, lock, pila))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\n🧠 Pila de llamadas:")
    for evento in pila:
        print(f" - {evento}")
