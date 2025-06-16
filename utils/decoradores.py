def bonificar_agente(func):
    def wrapper(agente, *args, **kwargs):
        stats = agente.obtener_estadisticas()
        if stats['exitosas'] >= 5:
            print(f"🎉 Agente {agente.nombre} ha sido bonificado por alto desempeño.")
        return func(agente, *args, **kwargs)
    return wrapper
