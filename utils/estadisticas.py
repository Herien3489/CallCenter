import csv
import os
import matplotlib.pyplot as plt

def mostrar_graficas_estadisticas(ruta_csv="archivos/estadisticas.csv"):
    if not os.path.exists(ruta_csv):
        print("⚠️ No se encontró el archivo de estadísticas.")
        return

    agente_buscado = input("🔎 Ingresa el nombre del agente: ").strip()

    llamadas = []
    with open(ruta_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["agente"].strip().lower() == agente_buscado.lower():
                exitosa = fila["exitosa"].lower() == "true"
                llamadas.append({
                    "cliente": fila["cliente"],
                    "duracion": int(fila["duracion"]),
                    "exitosa": exitosa
                })

    if not llamadas:
        print(f"⚠️ No se encontraron llamadas para el agente '{agente_buscado}'.")
        return

    total = len(llamadas)
    exitosas = sum(1 for l in llamadas if l["exitosa"])
    fallidas = total - exitosas
    efectividad = (exitosas / total) * 100
    duraciones = [l["duracion"] for l in llamadas]

    # Crear carpeta si no existe
    os.makedirs("graficas", exist_ok=True)

    # Gráfico de barras de llamadas exitosas/fallidas
    plt.figure()
    plt.bar(["Exitosas", "Fallidas"], [exitosas, fallidas])
    plt.title(f"Resultados de llamadas - {agente_buscado}")
    plt.ylabel("Cantidad")
    plt.savefig(f"graficas/resultados_{agente_buscado}.png")
    plt.show()

    # Gráfico de duración de llamadas
    plt.figure()
    plt.plot(duraciones, marker='o')
    plt.title(f"Duración de llamadas - {agente_buscado}")
    plt.xlabel("N° de llamada")
    plt.ylabel("Duración (segundos)")
    plt.savefig(f"graficas/duracion_{agente_buscado}.png")
    plt.show()

    print(f"✅ Gráficas del agente '{agente_buscado}' generadas.")
