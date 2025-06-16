from utils.estadisticas import estadisticas_por_campania

def mostrar_estadisticas_campania(campania):
    stats = estadisticas_por_campania(campania)
    print(f"\n📢 Campaña: {campania.nombre}")
    print(f"Total llamadas: {stats['total']}")
    print(f"Llamadas exitosas: {stats['exitosas']}")
    print(f"Efectividad: {stats['efectividad']:.2f}%")
