import networkx as nx

class SistemaViajes:
    def __init__(self, archivo_rutas):
        self.grafo = self.cargar_rutas(archivo_rutas)
    
    def cargar_rutas(self, nombre_archivo):
        grafo = nx.Graph()
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                estacion_origen, estacion_destino, costo = linea.strip().split(', ')
                costo = int(costo)
                grafo.add_edge(estacion_origen, estacion_destino, weight=costo)
        return grafo

    def mapa_destinos(self, estacion_salida):
        destinos = list(self.grafo.neighbors(estacion_salida))
        print(f"Posibles destinos desde {estacion_salida}:")
        for destino in destinos:
            print(destino)

    def dijkstra(self, estacion_salida):
        distancias = nx.single_source_dijkstra_path_length(self.grafo, estacion_salida)
        rutas = nx.single_source_dijkstra_path(self.grafo, estacion_salida)
        print("Mejores rutas desde", estacion_salida)
        for destino in distancias:
            if destino != estacion_salida:
                print(f"Destino: {destino}, Costo: {distancias[destino]}, Ruta: {rutas[destino]}")

class Programa:
    def __init__(self):
        self.sistema = SistemaViajes("rutas.txt")
        
    def ejecutar(self):
        print("Bienvenido al sistema de agendamiento de viajes.")
        estacion_salida = input("Por favor ingresa la estación de salida: ")

        if estacion_salida not in self.sistema.grafo.nodes():
            print("La estación de salida no existe en el sistema.")
        else:
            self.sistema.mapa_destinos(estacion_salida)
            self.sistema.dijkstra(estacion_salida)

if __name__ == "__main__":
    programa = Programa()
    programa.ejecutar()

