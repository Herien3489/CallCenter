import threading
import time
import random
from statistics import mean

class Llamada:
    _id_counter = 1  # ✅ Define el contador aquí

    def __init__(self, agente, duracion, exitosa, observacion=""):
        self.id = Llamada._id_counter
        Llamada._id_counter += 1
        self.agente = agente
        self.duracion = duracion
        self.exitosa = exitosa
        self.observacion = observacion
        
    
    def __str__(self):
        resultado = "ÉXITO" if self.exitosa else "FALLO"
        return f"[#{self.id}] {self.agente.nombre} - {resultado} - {self.duracion}s - {self.observacion}"
    # def simular_llamada(agente, lock):
    #     print(f"Iniciando llamada para {agente.nombre}...")

    #     duracion = random.randint(3, 8)  # segundos simulados
    #     time.sleep(duracion)

    #     exitosa = random.choice([True, False])
    #     observacion = "Cliente interesado" if exitosa else "Cliente colgó"

    #     llamada = Llamada(agente, duracion, exitosa, observacion)

    #     with lock:  # asegurar acceso seguro
    #         agente.registrar_llamada(llamada)
    #         print(f"Finalizó llamada ({'✔' if exitosa else '✘'}) de {duracion}s para {agente.nombre}")
class LlamadaManager:
    def __init__(self):
        self.llamadas = []

    def alta_llamada(self, llamada):
        self.llamadas.append(llamada)
        llamada.agente.registrar_llamada(llamada)
        print(f"✔ Llamada {llamada.id} registrada.")

    def baja_llamada(self, id_llamada):
        for i, llamada in enumerate(self.llamadas):
            if llamada.id == id_llamada:
                self.llamadas.pop(i)
                llamada.agente.llamadas = [l for l in llamada.agente.llamadas if l.id != id_llamada]
                print(f"🗑 Llamada {id_llamada} eliminada.")
                return
        print(f"❌ Llamada con ID {id_llamada} no encontrada.")

    def modificar_llamada(self, id_llamada, nueva_duracion=None, nuevo_resultado=None, nueva_observacion=None):
        for llamada in self.llamadas:
            if llamada.id == id_llamada:
                if nueva_duracion is not None:
                    llamada.duracion = nueva_duracion
                if nuevo_resultado is not None:
                    llamada.exitosa = nuevo_resultado
                if nueva_observacion is not None:
                    llamada.observacion = nueva_observacion
                print(f"✏️ Llamada {id_llamada} modificada.")
                return
        print(f"❌ Llamada con ID {id_llamada} no encontrada.")

    def listar_llamadas(self):
        if not self.llamadas:
            print("📭 No hay llamadas registradas.")
        else:
            for llamada in self.llamadas:
                print(llamada)
    def asignar_llamadas_automaticas(agentes, manager, total_llamadas=10):
        activos = [a for a in agentes if a.estado == "activo"]
        if not activos:
            print("❌ No hay agentes activos disponibles.")
            return

        lock = threading.Lock()
        threads = []

        # Distribución por ronda
        for i in range(total_llamadas):
            agente = activos[i % len(activos)]  # asignación equitativa
            hilo = threading.Thread(target=simular_llamada, args=(agente, manager, lock))
            threads.append(hilo)
            hilo.start()

        for hilo in threads:
            hilo.join()

        print("📞 Todas las llamadas fueron simuladas.")


              
def simular_llamada(agente, manager, lock):
    print(f"📞 Iniciando llamada para {agente.nombre}...")

    duracion = random.randint(3, 8)
    time.sleep(duracion)

    exitosa = random.choice([True, False])

    # Observaciones simuladas
    observaciones_positivas = ["Cliente interesado", "Agendó reunión", "Aceptó oferta"]
    observaciones_negativas = ["Cliente colgó", "No le interesa", "Número equivocado"]

    observacion = random.choice(observaciones_positivas if exitosa else observaciones_negativas)

    llamada = Llamada(agente, duracion, exitosa, observacion)

    with lock:
        manager.alta_llamada(llamada)
        print(f"✅ Finalizó llamada ({'✔' if exitosa else '✘'}) de {duracion}s para {agente.nombre} - Obs: {observacion}")
