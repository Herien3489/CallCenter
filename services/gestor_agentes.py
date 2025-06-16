from utils.estadisticas import estadisticas_por_agente
from utils.decoradores import bonificar_agente

@bonificar_agente
def mostrar_estadisticas_agente(agente):
    stats = estadisticas_por_agente(agente)
    print(f"\n📊 Estadísticas del agente {agente.nombre}")
    print(f"Total llamadas: {stats['total']}")
    print(f"Exitosas: {stats['exitosas']}")
    print(f"Fallidas: {stats['fallidas']}")
    print(f"Efectividad: {stats['efectividad']:.2f}%")
    print(f"Promedio duración: {stats['promedio_duracion']:.2f} segundos")
