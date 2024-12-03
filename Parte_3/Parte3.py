def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as file:
        lineas = [linea.strip() for linea in file if not linea.strip().startswith('#')]
        
        indices_lineas_blancas = [i for i, linea in enumerate(lineas) if linea == '']
        
        demandas_filas = [int(linea) for linea in lineas[:indices_lineas_blancas[0]]]
        demandas_columnas = [int(linea) for linea in lineas[indices_lineas_blancas[0]+1:indices_lineas_blancas[1]]]
        largos_barcos = [int(linea) for linea in lineas[indices_lineas_blancas[1]+1:] if linea]
        
        return demandas_filas, demandas_columnas, largos_barcos


def imprimir_tablero(tablero):
    for fila in tablero:
        print("  ".join(str(celda) if celda != 0 else '-' for celda in fila))

def batalla_naval_individual(largo_barcos, demandas_filas, demandas_columnas):
    n = len(demandas_filas)
    m = len(demandas_columnas)

    tablero = [[0 for _ in range(m)] for _ in range(n)]
    largo_barcos.sort(reverse=True)
    solucion = [tablero, float('inf')]

    batalla_naval_individual_backtracking(tablero, largo_barcos, demandas_filas, demandas_columnas, solucion)

    imprimir_tablero(solucion[0])
    
    demanda_total = sum(demandas_filas) + sum(demandas_columnas)
    demanda_cumplida = demanda_total - solucion[1]

    return demanda_cumplida, demanda_total


def batalla_naval_individual_backtracking(tablero, largo_barcos, demandas_filas, demandas_columnas, solucion):
    demanda_inicial = sum(demandas_filas) + sum(demandas_columnas)

    if demanda_inicial < solucion[1]:
        solucion[0] = [list(row) for row in tablero]
        solucion[1] = demanda_inicial
    if not largo_barcos:
        return
    if solucion[1] <= demanda_inicial - sum(barco * 2 for barco in largo_barcos):
        return
    
    batalla_naval_individual_backtracking(tablero, largo_barcos[1:], demandas_filas, demandas_columnas, solucion)

    for i in range(len(tablero)):
        if demandas_filas[i] > 0:
            for j in range(len(tablero[0])):
                if demandas_columnas[j] > 0:
                    procesar_barco(tablero, largo_barcos, i, j, demandas_filas, demandas_columnas, solucion, True)
                    procesar_barco(tablero, largo_barcos, i, j, demandas_filas, demandas_columnas, solucion, False)
        

def procesar_barco(tablero, largo_barcos, fila, columna, demandas_filas, demandas_columnas, solucion, es_horizontal):
    if intentar_colocar_barco(tablero, fila, columna, largo_barcos[0], es_horizontal, demandas_filas, demandas_columnas):
        colocar_barco(tablero, fila, columna, largo_barcos[0], demandas_filas, demandas_columnas, es_horizontal)
        batalla_naval_individual_backtracking(tablero, largo_barcos[1:], demandas_filas, demandas_columnas, solucion)
        quitar_barco(tablero, fila, columna, largo_barcos[0], demandas_filas, demandas_columnas, es_horizontal)


def colocar_barco(tablero, fila, columna, largos_barco, demandas_filas, demandas_columnas, es_horizontal):
 
    if es_horizontal:
        for i in range(columna, columna + largos_barco):
            tablero[fila][i] = 1
        demandas_filas[fila] -= largos_barco
        for i in range(columna, columna + largos_barco):
            demandas_columnas[i] -= 1
    else:
        for i in range(fila, fila + largos_barco):
            tablero[i][columna] = 1
        demandas_columnas[columna] -= largos_barco
        for i in range(fila, fila + largos_barco):
            demandas_filas[i] -= 1


def quitar_barco(tablero, fila, columna, largos_barco, demandas_filas, demandas_columnas, es_horizontal):

    if es_horizontal:
        for i in range(columna, columna + largos_barco):
            tablero[fila][i] = 0
        demandas_filas[fila] += largos_barco
        for i in range(columna, columna + largos_barco):
            demandas_columnas[i] += 1
    else:
        for i in range(fila, fila + largos_barco):
            tablero[i][columna] = 0
        demandas_columnas[columna] += largos_barco
        for i in range(fila, fila + largos_barco):
            demandas_filas[i] += 1


def verificar_limites_barco(tablero, fila, columna, largo, es_horizontal):
    """
    Verifica si un barco cabe dentro de los límites del tablero.
    """
    n, m = len(tablero), len(tablero[0])
    
    if es_horizontal:
        return columna + largo <= m
    else:
        return fila + largo <= n


def verificar_ocupacion_adyacente(tablero, fila, columna, largo, es_horizontal):
    n, m = len(tablero), len(tablero[0])
    
    for i in range(largo):
        fil, col = (fila, columna + i) if es_horizontal else (fila + i, columna)
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nueva_fila = fil + dx
                nueva_columna = col + dy
                
                if (dx != 0 or dy != 0) and 0 <= nueva_fila < n and 0 <= nueva_columna < m:
                    if tablero[nueva_fila][nueva_columna] != 0:
                        return False
    
    return True


def intentar_colocar_barco(tablero, fila, columna, largo, es_horizontal, demandas_filas, demandas_columnas):
    if not verificar_limites_barco(tablero, fila, columna, largo, es_horizontal):
        return False
    
    if es_horizontal:
        if demandas_filas[fila] < largo or any(demandas_columnas[columna + i] < 1 for i in range(largo)):
            return False
    else:
        if demandas_columnas[columna] < largo or any(demandas_filas[fila + i] < 1 for i in range(largo)):
            return False
    
    casillas_ocupadas = any(
        tablero[fila + i][columna] if not es_horizontal else tablero[fila][columna + i]
        for i in range(largo)
    )
    if casillas_ocupadas:
        return False
    
    return verificar_ocupacion_adyacente(tablero, fila, columna, largo, es_horizontal)


def main():

    import sys
    
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo.")
        return
    
    ruta_archivo = sys.argv[1]
    
    demandas_filas, demandas_columnas, largos_barcos = leer_archivo(ruta_archivo)
    
    n = len(demandas_filas)
    m = len(demandas_columnas)
    
    demanda_cumplida, demanda_total = batalla_naval_individual(largos_barcos, demandas_filas, demandas_columnas)
    
    print(f"Demanda cumplida: {demanda_cumplida}")
    print(f"Demanda total: {demanda_total}")


if __name__ == "__main__":
    main()