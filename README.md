
# Sistema de Agendamiento de Viajes

Este programa implementa un sistema para agendar viajes utilizando Python. Permite cargar un archivo de rutas y luego proporciona funcionalidades como mostrar un mapa de posibles destinos desde una estación de salida y encontrar las mejores rutas utilizando el algoritmo de Dijkstra.

## Requisitos

- Python 3.x
- Biblioteca NetworkX
- Biblioteca Matplotlib

Puedes instalar las bibliotecas necesarias utilizando pip:

```
pip install networkx matplotlib
```

## Uso

1. Ejecuta el programa ejecutando el script `main.py`.
2. El programa te pedirá que ingreses la estación de salida.
3. Después de ingresar la estación de salida, el programa mostrará un mapa de posibles destinos y las mejores rutas para llegar a cada destino.

## Formato del archivo de rutas

El programa espera un archivo de texto llamado `rutas.txt` con el siguiente formato:

```
"Estación de salida", "Estación de destino", costo
"Estación de salida", "Estación de destino", costo
...
```

Por ejemplo:

```
"Pueblo Paleta", "Aldea Azalea", 100
"Aldea Azalea", "Ciudad Safiro", 150
"Pueblo Paleta", "Ciudad Safiro", 800
"Ciudad Lavanda", "Aldea Fuego", 300
```

## Notas

- Todas las rutas son simétricas, lo que significa que si hay una ruta de X a Y, también hay una ruta de Y a X con el mismo costo.
- El programa utiliza la biblioteca NetworkX para representar y analizar el grafo de rutas.
- La implementación del algoritmo de Dijkstra está incorporada en la biblioteca NetworkX y se utiliza para encontrar las mejores rutas desde la estación de salida.
- para ver los datos escritos cerrar el matplotlib
