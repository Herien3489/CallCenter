import matplotlib.pyplot as plt
import json
from collections import defaultdict

class ReporteEstadistico:
    def __init__(self, llamadas):
        self.llamadas = llamadas

    def generar_graficas(self):
        if not self.llamadas:
            print("📭 No hay llamadas registradas.")
            return

        llamadas_por_agente = defaultdict(list)
        for llamada in self.llamadas:
            llamadas_por_agente[llamada.agente.nombre].append(llamada)

        nombres = []
        total_llamadas = []
        exitosas = []
        tasas_exito = []

        for nombre, llamadas in llamadas_por_agente.items():
            nombres.append(nombre)
            total = len(llamadas)
            exito = len([l for l in llamadas if l.exitosa])
            tasa = (exito / total) * 100 if total > 0 else 0

            total_llamadas.append(total)
            exitosas.append(exito)
            tasas_exito.append(tasa)

        # --- Gráfico 1: Total de llamadas (Productividad)
        plt.figure(figsize=(8, 4))
        plt.bar(nombres, total_llamadas)
        plt.title("📊 Productividad por agente")
        plt.ylabel("Total de llamadas")
        plt.xlabel("Agente")
        plt.tight_layout()
        plt.savefig("graficos/productividad.png")
        plt.show()

        # --- Gráfico 2: Tasa de éxito por agente
        plt.figure(figsize=(8, 4))
        plt.bar(nombres, tasas_exito)
        plt.title("✅ Tasa de Éxito (%) por Agente")
        plt.ylabel("Porcentaje de llamadas exitosas")
        plt.xlabel("Agente")
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.savefig("graficos/tasa_exito.png")
        plt.show()

        # --- Gráfico 3: Comparativa de carga
        plt.figure(figsize=(8, 4))
        plt.bar(nombres, total_llamadas, label="Total")
        plt.bar(nombres, exitosas, label="Exitosas")
        plt.title("📉 Carga de llamadas por agente")
        plt.ylabel("Cantidad de llamadas")
        plt.xlabel("Agente")
        plt.legend()
        plt.tight_layout()
        plt.savefig("graficos/carga_por_agente.png")
        plt.show()

    def exportar_txt_json(self, nombre_base="registro_llamadas"):
        if not self.llamadas:
            print("❌ No hay llamadas para exportar.")
            return

        # Exportar a .txt
        with open(f"{nombre_base}.txt", "w", encoding="utf-8") as f:
            for l in self.llamadas:
                f.write(f"{l.id},{l.agente.nombre},{l.duracion},{l.exitosa},{l.observacion}\n")

        # Exportar a .json
        llamadas_json = [{
            "id": l.id,
            "agente": l.agente.nombre,
            "duracion": l.duracion,
            "exitosa": l.exitosa,
            "observacion": l.observacion
        } for l in self.llamadas]

        with open(f"{nombre_base}.json", "w", encoding="utf-8") as f:
            json.dump(llamadas_json, f, indent=4)

        print(f"✅ Exportado a {nombre_base}.txt y {nombre_base}.json")
