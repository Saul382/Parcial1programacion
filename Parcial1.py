# En El Salvador, muchas personas dependen del transporte público para ir
# a su trabajo, estudio o actividades diarias. Cada día realizan distintos viajes
# en rutas urbanas o rurales, con tiempos y costos variables. Sin un registro,
# es difícil saber cuánto se gasta en transporte semanalmente ni cuáles rutas
# consumen más tiempo o dinero.

# ---------------------------------------------------------------------------
# Este programa permite registrar rutas y viajes de transporte público.
# El usuario puede:
#   1. Agregar rutas (nombre, tipo, costo y tiempo estimado).
#   2. Registrar los días en que usa cada ruta.
#   3. Consultar un resumen de todas las rutas, los días de uso,
#      el gasto semanal, la ruta más costosa y la más lenta.
# Use el menú para navegar por las opciones y siga las instrucciones en pantalla.
# ---------------------------------------------------------------------------

from Rutas import Ruta
from Viajes import Viaje
from Registro import RegistroTransporte

def pedir_ruta():
    # Solicita los datos de una nueva ruta al usuario y devuelve una instancia de Ruta.
    nombre = input("Nombre de la ruta: ")
    tipo = input("Tipo de ruta (urbana/rural): ")
    costo = float(input("Costo de la ruta: "))
    tiempo = int(input("Tiempo estimado (minutos): "))
    return Ruta(nombre, tipo, costo, tiempo)

def pedir_viaje(rutas):
    # Permite al usuario seleccionar una ruta y registrar uno o varios días de viaje para esa ruta.
    print("Rutas disponibles:")
    for idx, ruta in enumerate(rutas):
        print(f"{idx+1}. {ruta.nombre} ({ruta.tipo})")
    idx = int(input("Seleccione el número de la ruta: ")) - 1
    dias = []
    while True:
        dia = input("Día del viaje: ")
        dias.append(dia)
        otro = input("¿Desea agregar otro día para esta ruta? (s/n): ").lower()
        if otro != "s":
            break
    # Devuelve una lista de tuplas (ruta, día)
    return [(rutas[idx], d) for d in dias]

def main():
    # Función principal que muestra el menú y gestiona la interacción con el usuario.
    rutas = [] # Lista de rutas registradas
    registro = RegistroTransporte() # Registro de todos los viajes

    while True:
        print("\n1. Agregar ruta")
        print("2. Agregar viaje")
        print("3. Mostrar resultados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar una nueva ruta
            ruta = pedir_ruta()
            rutas.append(ruta)
            print("Ruta agregada.")
        elif opcion == "2":
            # Agregar uno o varios viajes
            if not rutas:
                print("Primero agregue al menos una ruta.")
                continue
            while True:
                viajes = pedir_viaje(rutas)
                for ruta, dia in viajes:
                    viaje = Viaje(ruta, dia)
                    registro.agregar_viaje(viaje)
                otro = input("¿Desea agregar viajes para otra ruta? (s/n): ").lower()
                if otro != "s":
                    break
            print("Viaje(s) agregado(s).")
        elif opcion == "3":
            # Mostrar información de las rutas y estadísticas
            print("\n--- Viajes realizados (ordenados) ---")
            for idx, v in enumerate(registro.viajes, 1):
                print(f"{idx}. Ruta: {v.ruta.nombre} | Tipo: {v.ruta.tipo} | Costo: {v.ruta.costo} | Tiempo: {v.ruta.tiempo_estimado} min | Día: {v.dia}")
            print("-" * 40)
            gasto_total = registro.gasto_semanal()
            tiempo_total = sum(v.ruta.tiempo_estimado for v in registro.viajes)
            print(f"Gasto total semanal: ${gasto_total}")
            print(f"Tiempo total invertido: {tiempo_total} minutos")
        elif opcion == "4":
            # Salir del programa
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    # Punto de entrada
    main()
