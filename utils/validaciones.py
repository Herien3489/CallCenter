

def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def validar_agente(nombre, edad):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if not es_entero(edad) or int(edad) <= 0:
        return False, "La edad debe ser un número entero positivo."
    return True, ""

def validar_archivo_extension(nombre_archivo, extensiones_validas):
    return any(nombre_archivo.endswith(ext) for ext in extensiones_validas)
