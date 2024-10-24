"""
Ecuación de recurrencia: max(Opt(i-2) + numero actual, Opt(i-1))
"""

def reconstruccion(vector, solucion, tamaño):
    #La reconstrucción no esta del todo bien
    elecciones = []

    i = 0
    if solucion[tamaño] != solucion[tamaño-1]:
        i = tamaño
    else:
        i = tamaño-1

    while i >= 0:
        if i == 0:
            elecciones.append(vector[0])
        else:
            elecciones.append(vector[i-1])
        i -= 2

    elecciones.reverse()
    return elecciones

def pd_parte2(vector, tamaño):
    solucion = [0] * (tamaño+1)

    for i in range(1, tamaño+1):
        solucion[i] = max(solucion[i-2] + vector[i-1], solucion[i-1])

    return solucion

def main():
    vector = [10, 10, 15, 10, 10, 100, 10, 10, 10, 20]
    solucion = pd_parte2(vector, len(vector))
    print(solucion[len(vector)])
    print(reconstruccion(vector, solucion, len(vector)))

main()
