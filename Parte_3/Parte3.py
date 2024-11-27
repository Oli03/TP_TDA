def leer_archivo(ruta_archivo):
    """
    Lee el archivo, saltándose las líneas que comienzan con #
    y separa las demandas de filas, columnas y longitud de barcos
    """
    with open(ruta_archivo, 'r') as file:
        # Leer líneas, ignorando comentarios
        lineas = [linea.strip() for linea in file if not linea.strip().startswith('#')]
        
        # Encontrar índices de líneas en blanco
        indices_lineas_blancas = [i for i, linea in enumerate(lineas) if linea == '']
        
        # Separar secciones
        demandas_filas = [int(linea) for linea in lineas[:indices_lineas_blancas[0]]]
        demandas_columnas = [int(linea) for linea in lineas[indices_lineas_blancas[0]+1:indices_lineas_blancas[1]]]
        largos_barcos = [int(linea) for linea in lineas[indices_lineas_blancas[1]+1:] if linea]
        
        return demandas_filas, demandas_columnas, largos_barcos

def es_posicion_valida(tablero, fila, columna, largo, direccion):
    """
    Verifica si se puede colocar un barco en una posición dada
    sin tocar otros barcos horizontal, vertical o diagonalmente
    """
    n, m = len(tablero), len(tablero[0])
    
    # Definir los posibles incrementos según la dirección
    incrementos = {
        'horizontal': (0, 1),
        'vertical': (1, 0)
    }
    
    df, dc = incrementos[direccion]
    
    # Verificar los límites del tablero
    if (fila + df * (largo-1) < 0 or fila + df * (largo-1) >= n or
        columna + dc * (largo-1) < 0 or columna + dc * (largo-1) >= m):
        return False
    
    # Verificar si hay espacio para el barco y sus alrededores
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(largo):
                nueva_fila = fila + df * k + i
                nueva_columna = columna + dc * k + j
                
                # Verificar límites del tablero
                if (0 <= nueva_fila < n and 0 <= nueva_columna < m):
                    # Si hay un barco en cualquier posición cercana, no es válido
                    if tablero[nueva_fila][nueva_columna] != 0:
                        return False
    
    return True

def colocar_barco(tablero, barco, posiciones, demandas_filas, demandas_columnas):
    """
    Función de backtracking para colocar los barcos
    """
    # Si ya se colocaron todos los barcos, retornar True
    if barco == len(posiciones):
        return True
    
    n, m = len(tablero), len(tablero[0])
    largo_barco = posiciones[barco]
    
    # Probar colocar el barco en horizontal y vertical
    for direccion in ['horizontal', 'vertical']:
        for fila in range(n):
            for columna in range(m):
                # Si la posición es válida y no excede las demandas
                if (es_posicion_valida(tablero, fila, columna, largo_barco, direccion) and
                    puede_colocar_barco(tablero, fila, columna, largo_barco, direccion, 
                                        demandas_filas, demandas_columnas)):
                    
                    # Marcar el barco en el tablero
                    for k in range(largo_barco):
                        if direccion == 'horizontal':
                            tablero[fila][columna + k] = barco + 1
                        else:
                            tablero[fila + k][columna] = barco + 1
                    
                    # Registrar la posición del barco
                    resultados[barco] = (fila, columna) if largo_barco == 1 else (fila, columna, 
                                         fila + (1 if direccion == 'vertical' else 0), 
                                         columna + (1 if direccion == 'horizontal' else 0))
                    
                    # Intentar colocar el siguiente barco
                    if colocar_barco(tablero, barco + 1, posiciones, demandas_filas, demandas_columnas):
                        return True
                    
                    # Deshacer la colocación del barco si no funciona
                    for k in range(largo_barco):
                        if direccion == 'horizontal':
                            tablero[fila][columna + k] = 0
                        else:
                            tablero[fila + k][columna] = 0
                    
                    resultados[barco] = None
    
    return False

def puede_colocar_barco(tablero, fila, columna, largo, direccion, demandas_filas, demandas_columnas):
    """
    Verifica si colocar este barco no excede las demandas de filas y columnas
    """
    n, m = len(tablero), len(tablero[0])
    
    # Contar ocupaciones actuales de filas y columnas
    ocupacion_filas = [sum(1 for cell in row if cell != 0) for row in tablero]
    ocupacion_columnas = [sum(1 for row in tablero for cell in [row[j]] if cell != 0) for j in range(m)]
    
    # Verificar para la dirección horizontal
    if direccion == 'horizontal':
        # Revisar la demanda de la fila actual
        if ocupacion_filas[fila] + largo > demandas_filas[fila]:
            return False
        
        # Revisar la demanda de las columnas
        for k in range(largo):
            if ocupacion_columnas[columna + k] + 1 > demandas_columnas[columna + k]:
                return False
    
    # Verificar para la dirección vertical
    else:  # vertical
        # Revisar la demanda de las filas
        for k in range(largo):
            if ocupacion_filas[fila + k] + 1 > demandas_filas[fila + k]:
                return False
        
        # Revisar la demanda de la columna actual
        if ocupacion_columnas[columna] + largo > demandas_columnas[columna]:
            return False
    
    return True

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo.")
        return
    
    ruta_archivo = sys.argv[1]
    
    # Leer datos del archivo
    demandas_filas, demandas_columnas, largos_barcos = leer_archivo(ruta_archivo)
    
    # Determinar tamaño del tablero (puede ser ajustado según necesidad)
    n = len(demandas_filas)
    m = len(demandas_columnas)
    
    # Crear tablero inicialmente vacío
    tablero = [[0 for _ in range(m)] for _ in range(n)]
    
    # Variable global para guardar resultados
    global resultados
    resultados = [None] * len(largos_barcos)
    
    # Intentar colocar los barcos
    colocar_barco(tablero, 0, largos_barcos, demandas_filas, demandas_columnas)
    
    # Mostrar resultados
    print("Posiciones:")
    for i, pos in enumerate(resultados):
        print(f"{i}: {pos}")
    
    # Calcular demanda cumplida
    demanda_cumplida = sum(1 if pos is not None else 0 for pos in resultados)
    demanda_total = sum(demandas_filas) + sum(demandas_columnas)
    
    print(f"Demanda cumplida: {demanda_cumplida}")
    print(f"Demanda total: {demanda_total}")

if __name__ == "__main__":
    main()