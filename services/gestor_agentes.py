from models.agente import AgenteJunior, AgenteSenior

# Lista global de agentes
agentes = []

def agregar_agente(nombre, edad, tipo="Junior"):
    if tipo.lower() == "junior":
        agente = AgenteJunior(nombre, edad)
    elif tipo.lower() == "senior":
        agente = AgenteSenior(nombre, edad)
    else:
        print(f"⚠️ Tipo de agente inválido: '{tipo}'")
        return
    agentes.append(agente)
    print(f"✅ Agente {nombre} ({tipo}) agregado correctamente.")

def eliminar_agente(nombre):
    global agentes
    antes = len(agentes)
    agentes = [a for a in agentes if a.nombre != nombre]
    if len(agentes) < antes:
        print(f"🗑️ Agente '{nombre}' eliminado.")
    else:
        print(f"⚠️ Agente '{nombre}' no encontrado.")

def listar_agentes():
    if not agentes:
        print("⚠️ No hay agentes registrados.")
        return
    print("📋 Lista de agentes:")
    for i, agente in enumerate(agentes, start=1):
        print(f"{i}. {agente.nombre} - {agente.obtener_tipo()} - Estado: {agente.estado}")

def buscar_agente(nombre):
    for agente in agentes:
        if agente.nombre == nombre:
            return agente
    print(f"⚠️ Agente '{nombre}' no encontrado.")
    return None

def cambiar_estado_agente(nombre, nuevo_estado):
    agente = buscar_agente(nombre)
    if agente:
        if nuevo_estado.lower() == "activo":
            agente.activar()
        elif nuevo_estado.lower() == "inactivo":
            agente.desactivar()
        else:
            print("⚠️ Estado inválido. Usa 'activo' o 'inactivo'.")
            return
        print(f"✅ Estado del agente '{nombre}' actualizado a {nuevo_estado}.")

def mostrar_estadisticas_agente(nombre):
    agente = buscar_agente(nombre)
    if agente:
        stats = agente.obtener_estadisticas()
        print(f"\n📊 Estadísticas de {agente.nombre}:")
        print(f" - Total llamadas: {stats['total']}")
        print(f" - Exitosas: {stats['exitosas']}")
        print(f" - Fallidas: {stats['fallidas']}")
        print(f" - Efectividad: {stats['efectividad']:.2f}%")
        print(f" - Duración promedio: {stats['promedio_duracion']:.2f} segundos")
