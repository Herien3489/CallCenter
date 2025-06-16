
import matplotlib.pyplot as plt
import os

def grafica_efectividad_por_agente(agentes, ruta_salida="graficos/efectividad.png"):
    nombres = [agente.nombre for agente in agentes]
    efectividades = [agente.obtener_estadisticas()['efectividad'] for agente in agentes]

    plt.figure(figsize=(10, 6))
    plt.bar(nombres, efectividades)
    plt.title("Efectividad por Agente (%)")
    plt.xlabel("Agente")
    plt.ylabel("Efectividad")
    plt.ylim(0, 100)
    plt.grid(axis='y')
    
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    plt.savefig(ruta_salida)
    plt.close()
    print(f"📊 Gráfico guardado en {ruta_salida}")
