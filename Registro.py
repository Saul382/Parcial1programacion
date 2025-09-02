from Viajes import Viaje

# Clase para registrar y analizar los viajes realizados en diferentes rutas.
class RegistroTransporte:
    def __init__(self):
        # Inicializa el registro con una lista vacía de viajes.
        self.viajes = []

    def agregar_viaje(self, viaje):
        # Agrega un viaje al registro.
        # :param viaje: Instancia de la clase Viaje.
        self.viajes.append(viaje)

    def gasto_semanal(self):
        # Calcula el gasto total semanal sumando el costo de todos los viajes registrados.
        # :return: Suma de los costos de los viajes (float).
        if not self.viajes:
            return 0
        return sum(getattr(v.ruta, 'costo', 0) for v in self.viajes)

    def ruta_mas_costosa(self):
        # Determina la ruta en la que se ha gastado más dinero en total.
        # Suma los costos de todos los viajes agrupados por nombre de ruta.
        # :return: Nombre de la ruta más costosa (str) o None si no hay viajes.
        if not self.viajes:
            return None
        costos = {}
        for v in self.viajes:
            nombre = getattr(v.ruta, 'nombre', 'Desconocido')
            costo = getattr(v.ruta, 'costo', 0)
            costos[nombre] = costos.get(nombre, 0) + costo
        return max(costos, key=costos.get)

    def ruta_mas_lenta(self):
        # Determina la ruta que ha consumido más tiempo en total.
        # Suma los tiempos estimados de todos los viajes agrupados por nombre de ruta.
        # :return: Nombre de la ruta más lenta (str) o None si no hay viajes.
        if not self.viajes:
            return None
        tiempos = {}
        for v in self.viajes:
            nombre = getattr(v.ruta, 'nombre', 'Desconocido')
            tiempo = getattr(v.ruta, 'tiempo_estimado', 0)
            tiempos[nombre] = tiempos.get(nombre, 0) + tiempo
        return max(tiempos, key=tiempos.get)
