from models.agente import AgenteJunior, AgenteSenior
import csv
import os
import json
# Lista global de agentes
agentes = []

RUTA_CSV = "archivos/agentes.csv"
RUTA_ESTADISTICAS = "archivos/estadisticas.json"

def agregar_agente(nombre, edad, tipo="Junior"):
    nombre = nombre.strip()
    tipo = tipo.strip().lower()

    if tipo == "junior":
        agente = AgenteJunior(nombre, edad)
    elif tipo == "senior":
        agente = AgenteSenior(nombre, edad)
    else:
        print(f"⚠️ Tipo de agente inválido: '{tipo}'")
        return

    # Validar si ya existe
    if any(a.nombre.lower() == nombre.lower() for a in agentes):
        print(f"⚠️ Ya existe un agente llamado {nombre}. No se agregó.")
        return

    # Agregar a la lista en memoria
    agentes.append(agente)
    print(f"✅ Agente {nombre} ({tipo.capitalize()}) agregado correctamente.")

    # Guardar en CSV
    existe = os.path.exists(RUTA_CSV)
    with open(RUTA_CSV, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        if not existe:
            escritor.writerow(["nombre", "edad", "tipo", "estado"])
        escritor.writerow([agente.nombre, agente.edad, tipo.capitalize(), agente.estado])

def eliminar_agente(nombre):
    global agentes
    nombre = nombre.strip().lower()
    antes = len(agentes)
    agentes = [a for a in agentes if a.nombre.strip().lower() != nombre]
    eliminado = len(agentes) < antes

    if not os.path.exists(RUTA_CSV):
        print("⚠️ El archivo CSV no existe.")
        return

    agentes_actualizados = []
    encontrado_en_csv = False

    with open(RUTA_CSV, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["nombre"].strip().lower() != nombre:
                agentes_actualizados.append(fila)
            else:
                encontrado_en_csv = True

    if encontrado_en_csv:
        with open(RUTA_CSV, "w", newline='', encoding="utf-8") as f:
            fieldnames = ["nombre", "edad", "tipo", "estado"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(agentes_actualizados)
        print(f"🗑️ Agente '{nombre}' eliminado del CSV y de memoria.")
    else:
        print(f"⚠️ Agente '{nombre}' no encontrado en el archivo CSV.")

# --- 2. Listar agentes ---
def listar_agentes():
    if not os.path.exists(RUTA_CSV):
        print("⚠️ El archivo de agentes no existe.")
        return

    with open(RUTA_CSV, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        agentes = list(lector)

    if not agentes:
        print("⚠️ No hay agentes registrados en el archivo.")
        return

    print("📋 Lista de agentes:")
    for i, agente in enumerate(agentes, start=1):
        print(f"{i}. {agente['nombre']} - {agente['tipo']} - Estado: {agente['estado']}")

# --- 3. Buscar agente por nombre (no sensible a mayúsculas) ---
def buscar_agente(nombre):
    for agente in agentes:
        if agente.nombre.lower() == nombre.lower():
            return agente
    print(f"⚠️ Agente '{nombre}' no encontrado.")
    return None

# --- 4. Cambiar estado del agente ---
def cambiar_estado_agente(nombre, nuevo_estado):
    nuevo_estado = nuevo_estado.lower()
    if nuevo_estado not in ["activo", "inactivo"]:
        print("⚠️ Estado inválido. Usa 'activo' o 'inactivo'.")
        return

    actualizado = False
    agentes_csv = []

    with open(RUTA_CSV, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["nombre"].lower() == nombre.lower():
                fila["estado"] = nuevo_estado
                actualizado = True
            agentes_csv.append(fila)

    if not actualizado:
        print(f"⚠️ Agente '{nombre}' no encontrado en el CSV.")
        return

    with open(RUTA_CSV, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["nombre", "edad", "tipo", "estado"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(agentes_csv)

    print(f"✅ Estado del agente '{nombre}' actualizado a {nuevo_estado}.")

# --- 5. Mostrar estadísticas del agente ---
def mostrar_estadisticas_agente(nombre):
    nombre = nombre.strip()

    if not os.path.exists(RUTA_ESTADISTICAS):
        print("⚠️ El archivo de estadísticas no existe.")
        return

    with open(RUTA_ESTADISTICAS, "r", encoding="utf-8") as f:
        datos = json.load(f)

    agente_data = datos.get(nombre)
    if not agente_data:
        print(f"⚠️ No hay estadísticas registradas para el agente '{nombre}'.")
        return

    stats = agente_data["estadisticas"]

    print(f"\n📊 Estadísticas de {nombre}:")
    print(f" - Edad: {agente_data['edad']}")
    print(f" - Estado: {agente_data['estado']}")
    print(f" - Total llamadas: {stats['total']}")
    print(f" - Exitosas: {stats['exitosas']}")
    print(f" - Fallidas: {stats['fallidas']}")
    print(f" - Efectividad: {stats['efectividad']:.2f}%")
    print(f" - Duración promedio: {stats['promedio_duracion']:.2f} segundos")

def cargar_agentes_desde_csv():
    global agentes
    agentes.clear()

    try:
        with open(RUTA_CSV, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                tipo = fila["tipo"].strip().lower()
                nombre = fila["nombre"].strip()
                edad = int(fila["edad"])
                estado = fila["estado"].strip().lower()

                if tipo == "junior":
                    agente = AgenteJunior(nombre, edad)
                elif tipo == "senior":
                    agente = AgenteSenior(nombre, edad)
                else:
                    continue  # ignora tipos inválidos
                
                

                agentes.append(agente)
        print(f"✅ {len(agentes)} agentes cargados desde el CSV.")

    except FileNotFoundError:
        print("⚠️ Archivo de agentes no encontrado.")

# --- 6. Guardar todos los agentes nuevamente al CSV ---
def _guardar_csv_agentes():
    with open(RUTA_CSV, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "edad", "tipo", "estado"])
        for a in agentes:
            tipo = a.obtener_tipo()  # debe existir este método en tus clases
            writer.writerow([a.nombre, a.edad, tipo, a.estado])