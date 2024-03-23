import random
from termcolor import colored

def Datos(matriz):    
    '''Extraer los datos "total", "vacios", "quemado", "vivos", "quemandose", "arbolesQuedan", de una matriz'''
    vivos = 0
    for fila in matriz:
        for i in fila:
            if i == -1:
                vivos +=  1
    quemados = 0
    for fila in matriz:
        for i in fila:
            if i == 0:
                quemados += 1
    vacios = 0
    for fila in matriz:
        for i in fila:
            if i == -2:
                vacios += 1
    total = 0
    for fila in matriz:
        for i in fila:
            total += 1
    quemandose = total - vacios - quemados - vivos
    arbolesQuedan = vivos + quemandose
    return total, vacios, quemados, vivos, quemandose, arbolesQuedan

def aColor(matriz):
    '''Cambiar los valores -1, -2, 0 y positivos por strings de colores de una matriz con la libreria termcolor'''
    green = colored("▓▓", "green")
    red = colored("▓▓", "red")
    white = colored("▓▓", "white")
    for fila in range(len(matriz)):
        for i in range(len(matriz[fila])):
            if matriz[fila][i] == -1:
                matriz[fila][i] = green
            elif matriz[fila][i] == -2:
                matriz[fila][i]  = "  "
            elif matriz[fila][i] == 0:
                matriz[fila][i]  = white
            elif matriz[fila][i] > 0:
                    matriz[fila][i]  = red
    return matriz

def Imprimir(matriz, t, quemandose, arbolesQuedan, quemados):
    '''
    Imprime la matriz y los datos de la misma.
    Toma los argumentos:
    - matriz
    - t = tiempo
    - quemandose = arboles quemandose
    - arbolesQuedan = arboles que quedan vivos
    - quemados = arboles ya quemados
    '''
    for fila in matriz:
        for i in fila:
            print(i, end='')
        print()
    print(f" t = {t} \n", colored(f"Árboles quemandose: {quemandose}", "red"), "\n", colored(f"Árboles que quedan: {arbolesQuedan}", "green"),"\n", colored(f"Árboles quemados: {quemados}", "white"), "\n")
    print("============================================================\n")

def Actualizar(matriz,p,tq):
    '''
    Función que actualiza cada celda de una matriz con las siguientes reglas:
    -Las celdas -2 y 0 quedan iguales
    -A las celdas positivas se les resta 1
    -Las celdas -1 se las cambia por la variable t(q), con una probabilidad p(x)
    Toma los argumentos: 
    - matriz
    - p = lista de probabilidades de que un -1 se vuelva un numero positivo según cuantos numeros positivos tiene alrededor
    - tq = un numero positivo
    '''
    matrizActualizada = [fila[:] for fila in matriz]
    for index, fila in enumerate(matriz):
        for i in range(len(fila)):
            if fila[i] == -2:
                continue
            elif fila[i] > 0:
                matrizActualizada[index][i] -= 1
            elif fila[i] == 0:
                continue
            elif fila[i] == -1:
                arboles = 0
                for y in range(max(0, index - 1), min(index + 2, len(matriz))):
                    for x in range(max(0, i - 1), min(i + 2, len(matriz[0]))):
                        if (y, x) != (fila, i):
                            if matriz[y][x] > 0:
                                arboles += 1
                if random.random() <= p[arboles]:
                    matrizActualizada[index][i] = tq
    return matrizActualizada
