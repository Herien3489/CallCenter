from services.gestor_agentes import (
    agregar_agente, eliminar_agente, listar_agentes,
    cambiar_estado_agente, mostrar_estadisticas_agente, agentes
)
from services.gestor_llamadas import ejecutar_llamadas_concurrentes
from utils.decoradores import bonificar_agentes
from models.cliente import Cliente

# Cargar clientes desde CSV
clientes = Cliente.cargar_desde_csv("archivos/clientes.csv")

def menu_agentes():
    while True:
        print("\n--- SUBMENÚ: GESTIÓN DE AGENTES ---")
        print("1. Agregar agente")
        print("2. Eliminar agente")
        print("3. Listar agentes")
        print("4. Cambiar estado de agente")
        print("5. Ver estadísticas de un agente")
        print("6. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre del agente: ")
            edad = input("Edad: ")
            tipo = input("Tipo (Junior/Senior): ")
            agregar_agente(nombre, edad, tipo)
        elif opcion == "2":
            nombre = input("Nombre del agente a eliminar: ")
            eliminar_agente(nombre)
        elif opcion == "3":
            listar_agentes()
        elif opcion == "4":
            nombre = input("Nombre del agente: ")
            estado = input("Nuevo estado (activo/inactivo): ")
            cambiar_estado_agente(nombre, estado)
        elif opcion == "5":
            nombre = input("Nombre del agente: ")
            mostrar_estadisticas_agente(nombre)
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")

def menu_principal():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Gestión de Agentes")
        print("2. Simular llamadas")
        print("3. Bonificar agentes destacados")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_agentes()
        elif opcion == "2":
            if not agentes:
                print("⚠️ Debes cargar/agregar agentes primero.")
                continue
            ejecutar_llamadas_concurrentes(agentes, clientes)
        elif opcion == "3":
            bonificar_agentes(agentes)
        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu_principal()
