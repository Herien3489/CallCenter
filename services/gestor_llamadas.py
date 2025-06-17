import threading
import random
import time
from models.llamada import Llamada
from models.cliente import Cliente
import csv
import os


# Suponemos que esta lista se pasa desde afuera o se carga antes
clientes = []

RUTA_ESTADISTICAS_CSV = "archivos/estadisticas.csv"

def simular_llamada(agente, lock, clientes, pila=None):
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

        # 📥 Registrar en estadisticas.csv
        existe = os.path.exists(RUTA_ESTADISTICAS_CSV)
        with open(RUTA_ESTADISTICAS_CSV, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["id", "agente", "cliente", "duracion", "exitosa", "observacion"])
            writer.writerow([
                llamada.id,
                agente.nombre,
                cliente.nombre,
                llamada.duracion,
                llamada.exitosa,
                llamada.observacion
            ])

    if pila is not None:
        pila.append(f"Finaliza llamada con {agente.nombre} a {cliente.nombre}")

def ejecutar_llamadas_concurrentes(agentes, lista_clientes):
    global clientes
    clientes = lista_clientes

    lock = threading.Lock()
    hilos = []
    pila = []

    for agente in agentes:
        hilo = threading.Thread(target=simular_llamada, args=(agente, lock, clientes, pila))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\n🧠 Registro de pila de llamadas:")
    for evento in pila:
        print("  -", evento)

    print("\n🧠 Pila de llamadas:")
    for evento in pila:
        print(f" - {evento}")
