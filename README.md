# TP_TDA
# Alumnos

- Oliver Weber 111138
- Agustín Reinaldo Colman Salinas 108804
- Miguel Angel Fonzalida 86125

# Trabajo Práctico: Juegos de Hermanos

Este proyecto implementa dos versiones del juego de monedas entre dos jugadores, Sophia y Mateo. Cada jugador elige monedas de un conjunto siguiendo reglas específicas para maximizar sus ganancias. La aplicación permite probar diferentes conjuntos de monedas almacenados en archivos dentro de las carpetas TP1_data y TP2_data.

## Contenido del Proyecto
* Parte 1: Sophia juega contra Mateo, quien es demasiado pequeño para entender el juego. Sophia elige las monedas por él, aplicando un algoritmo greedy para maximizar su propia ganancia.
* Parte 2: Mateo ahora juega por sí mismo, siguiendo una estrategia greedy. Sophia utiliza programación dinámica para maximizar su ganancia, anticipando las elecciones de Mateo.

## Estructura del Proyecto

### Parte 1
| Carpeta/Archivo              | Descripción                                          |
|------------------------------|------------------------------------------------------|
| `Parte_1/`                   | Carpeta principal que contiene el código fuente      |
| `Parte_1/Parte1.py`          | Código principal que ejecuta el juego de monedas     |
| `Parte_1/TP1_data/`          | Carpeta que contiene los archivos de datos de prueba |
| `Parte_1/TP1_data/20.txt`    | Archivo de prueba con 20 monedas                     |
| `Parte_1/TP1_data/25.txt`    | Archivo de prueba con 25 monedas                     |
| `Parte_1/TP1_data/50.txt`    | Archivo de prueba con 50 monedas                     |
| `Parte_1/TP1_data/100.txt`   | Archivo de prueba con 100 monedas                    |
| `Parte_1/TP1_data/1000.txt`  | Archivo de prueba con 1000 monedas                   |
| `Parte_1/TP1_data/10000.txt` | Archivo de prueba con 10000 monedas                  |
| `Parte_1/TP1_data/20000.txt` | Archivo de prueba con 20000 monedas                  |
| `Parte_1/TP1_data/Resultados Esperados.txt` | Resultados esperados para comparación |

### Parte 2
| Carpeta/Archivo              | Descripción                                          |
|------------------------------|------------------------------------------------------|
| `Parte_2/`                   | Carpeta principal que contiene el código fuente      |
| `Parte_2/Parte1.py`          | Código principal que ejecuta el juego de monedas     |
| `Parte_2/TP2_data/`          | Carpeta que contiene los archivos de datos de prueba |
| `Parte_2/TP2_data/5.txt`     | Archivo de prueba con 5 monedas                      |
| `Parte_2/TP2_data/10.txt`    | Archivo de prueba con 10 monedas                     |
| `Parte_2/TP2_data/20.txt`    | Archivo de prueba con 20 monedas                     |
| `Parte_2/TP2_data/25.txt`    | Archivo de prueba con 25 monedas                     |
| `Parte_2/TP2_data/50.txt`    | Archivo de prueba con 50 monedas                     |
| `Parte_2/TP2_data/100.txt`   | Archivo de prueba con 100 monedas                    |
| `Parte_2/TP2_data/1000.txt`  | Archivo de prueba con 1000 monedas                   |
| `Parte_2/TP2_data/2000.txt`   | Archivo de prueba con 2000 monedas                  |
| `Parte_2/TP2_data/5000.txt`  | Archivo de prueba con 5000 monedas                   |
| `Parte_2/TP2_data/10000.txt`   | Archivo de prueba con 10000 monedas                |
| `Parte_2/TP2_data/Resultados Esperados.txt` | Resultados esperados para comparación |

# Trabajo Práctico: La Batalla Naval Individual

Mateo aprendio a jugar con Programación Dinamica y el juego se volvio aburrido porque va a ganar siempre el que empieza el juego. Cada uno decidio jugar por su cuenta a otros juegos, en el caso de Sophia el juego que va a jugar va a ser la batalla naval individual. Este juego consiste en acomodar barcos en una grilla de una manera tal que se cumplan las restricciones de capacidad de las filas y las columnas.

## Contenido del Proyecto
* Primero se va a evaluar el problema si se puede reducir para ver si se puede resolver de manera polinomial y ver si se lo puede reducir a otro algoritmo NP-Completo.
* Luego, se intetara resolver el problema utilizando la tecnica de Backtracking.

## Estructura del Proyecto

### Parte 3
| Carpeta/Archivo                  | Descripción                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| `Parte_3/`                       | Carpeta principal que contiene el código fuente                                         |
| `Parte_3/Parte3.py`              | Código principal que ejecuta el juego de la batalla naval individual (Backtracking)     |
| `Parte_3/TP3_data/`              | Carpeta que contiene los archivos de datos de prueba                                    |
| `Parte_3/TP3_data/3_3_2.txt`     | Prueba 1#                                                                               |
| `Parte_3/TP3_data/5_5_6.txt`     | Prueba 2#                                                                               |
| `Parte_3/TP3_data/8_7_10.txt`    | Prueba 3#                                                                               |
| `Parte_3/TP3_data/10_3_3.txt`    | Prueba 4#                                                                               |
| `Parte_3/TP3_data/10_10_10.txt`  | Prueba 5#                                                                               |
| `Parte_3/TP3_data/12_12_21.txt`  | Prueba 6#                                                                               |
| `Parte_3/TP3_data/15_10_15.txt`  | Prueba 7#                                                                               |
| `Parte_3/TP3_data/20_20_20.txt`  | Prueba 8#                                                                               |
| `Parte_3/TP3_data/20_25_30.txt`  | Prueba 9#                                                                               |
| `Parte_3/TP3_data/30_25_25.txt`  | Prueba 10#                                                                              |
| `Parte_3/TP3_data/Resultados Esperados Tablero.txt` | Resultados esperados de los tableros                                 |
| `Parte_3/TP3_data/Resultados Esperados.txt` | Resultados esperados de las posiciones y las demandas                        |

## Requisitos

- **Python 3.6 o superior**: Verificar que Python esté instalado ejecutando:

  ```bash
    python --version
## Cómo Probar el Código
### Parte 1
Para probar el programa **Parte 1** con uno de los archivos de datos, siguir estos pasos:

- 1. Navegar a la Carpeta Correcta: 
     - Abrir un terminal y navegar a la carpeta Parte_1 donde se encuentra el archivo Parte1.py

      ```bash
        cd ruta/donde/estas/TP_TDA/Parte_1
    -  Reemplaza ruta/donde/estas con la ubicación real del proyecto.

- 2. Ejecutar el Programa:

    - Ejecutar el siguiente comando para probar el programa, especificando uno de los archivos de datos en TP1_data (por ejemplo, 20.txt):
    ```bash
        python Parte1.py TP1_data/20.txt
- Ejemplo de salida esperada:
El programa imprimirá:

- La secuencia de elecciones de monedas por Sophia y Mateo.
- La ganancia acumulada de cada jugador.
### Parte 2
Para probar el programa **Parte 2** con uno de los archivos de datos, siguir estos pasos:

- 1. Navegar a la Carpeta Correcta: 
     - Abrir un terminal y navegar a la carpeta Parte_2 donde se encuentra el archivo Parte2.py

      ```bash
        cd ruta/donde/estas/TP_TDA/Parte_2
    -  Reemplaza ruta/donde/estas con la ubicación real del proyecto.

- 2. Ejecutar el Programa:

    - Ejecutar el siguiente comando para probar el programa, especificando uno de los archivos de datos en TP2_data (por ejemplo, 20.txt):
    ```bash
        python Parte2.py TP2_data/20.txt
- Ejemplo de salida esperada:
El programa imprimirá:

- La secuencia de elecciones de monedas por Sophia y Mateo.
- La ganancia acumulada de cada jugador.

### Parte 3
Para probar el programa **Parte 3** con uno de los archivos de datos, siguir estos pasos:

- 1. Navegar a la Carpeta Correcta: 
     - Abrir un terminal y navegar a la carpeta Parte_3 donde se encuentra el archivo Parte3.py

      ```bash
        cd ruta/donde/estas/TP_TDA/Parte_3
    -  Reemplaza ruta/donde/estas con la ubicación real del proyecto.

- 2. Ejecutar el Programa:

    - Ejecutar el siguiente comando para probar el programa, especificando uno de los archivos de datos en TP3_data (por ejemplo, 3_3_2.txt):
    ```bash
        python Parte3.py TP3_data/3_3_2.txt
- Ejemplo de salida esperada:
El programa imprimirá:

- Un tablero de unos y ceros. Los unos indican que en esa posición se encuentran los barcos o las partes de los barcos.
- La demanda cumplida.
- La demanda total.
