import csv
from models.campaña import Campania
from utils.estadisticas import estadisticas_por_campania

campanias = []  # Lista global de campañas

def cargar_campanias_desde_csv(ruta):
    global campanias
    campanias = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila.get('nombre', '').strip()
            descripcion = fila.get('descripcion', '').strip()
            if nombre:
                campanias.append(Campania(nombre, descripcion))
    print(f"✅ Se cargaron {len(campanias)} campañas.")

def agregar_campania(nombre, descripcion):
    global campanias
    nueva = Campania(nombre, descripcion)
    campanias.append(nueva)
    print(f"✅ Campaña '{nombre}' agregada.")

def eliminar_campania(nombre):
    global campanias
    antes = len(campanias)
    campanias = [c for c in campanias if c.nombre != nombre]
    if len(campanias) < antes:
        print(f"🗑️ Campaña '{nombre}' eliminada.")
    else:
        print(f"⚠️ Campaña '{nombre}' no encontrada.")

def mostrar_todas():
    if not campanias:
        print("⚠️ No hay campañas cargadas.")
        return
    print("📋 Campañas actuales:")
    for c in campanias:
        print(f"- {c.nombre}: {c.descripcion}")

def mostrar_estadisticas_campania(nombre):
    global campanias
    for c in campanias:
        if c.nombre == nombre:
            stats = estadisticas_por_campania(c)
            print(f"\n📢 Estadísticas de campaña '{c.nombre}':")
            print(f"Total llamadas: {stats['total']}")
            print(f"Llamadas exitosas: {stats['exitosas']}")
            print(f"Efectividad: {stats['efectividad']:.2f}%")
            return
    print(f"⚠️ Campaña '{nombre}' no encontrada.")
