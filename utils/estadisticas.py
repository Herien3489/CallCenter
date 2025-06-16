from statistics import mean

# Estadísticas por agente
def estadisticas_agente(agente):
    total = len(agente.llamadas)
    exitosas = len([l for l in agente.llamadas if l.exitosa])
    fallidas = total - exitosas
    promedio_duracion = mean([l.duracion for l in agente.llamadas]) if agente.llamadas else 0
    efectividad = (exitosas / total) * 100 if total > 0 else 0

    return {
        "nombre": agente.nombre,
        "total_llamadas": total,
        "llamadas_exitosas": exitosas,
        "llamadas_fallidas": fallidas,
        "promedio_duracion": promedio_duracion,
        "efectividad": efectividad
    }

# Estadísticas globales de todos los agentes
def estadisticas_globales_agentes(lista_agentes):
    todas_llamadas = [l for a in lista_agentes for l in a.llamadas]
    if not todas_llamadas:
        return {}

    total = len(todas_llamadas)
    exitosas = len([l for l in todas_llamadas if l.exitosa])
    promedio_duracion = mean([l.duracion for l in todas_llamadas])
    efectividad = (exitosas / total) * 100

    return {
        "total_llamadas": total,
        "llamadas_exitosas": exitosas,
        "llamadas_fallidas": total - exitosas,
        "promedio_duracion_global": promedio_duracion,
        "efectividad_global": efectividad
    }

# Estadísticas por campaña (requiere llamadas asociadas a campañas)
def estadisticas_por_campaña(campaña):
    total = len(campaña.llamadas)
    exitosas = len([l for l in campaña.llamadas if l.exitosa])
    promedio_duracion = mean([l.duracion for l in campaña.llamadas]) if total > 0 else 0
    efectividad = (exitosas / total) * 100 if total > 0 else 0

    return {
        "nombre": campaña.nombre,
        "total_llamadas": total,
        "llamadas_exitosas": exitosas,
        "llamadas_fallidas": total - exitosas,
        "promedio_duracion": promedio_duracion,
        "efectividad": efectividad
    }
