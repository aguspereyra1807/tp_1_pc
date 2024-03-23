import random
from tp1_funciones_pereyra import Actualizar, Datos

def IncendioTiempo(n, d, tq, p):
    '''
    Realiza una simulación de un incendio de un bosque en una matriz con estos valores:
    -2 --> celda vacía.
    -1 --> arbol vivo.
    0 --> arbol quemado.
    numero positivo --> arbol quemandose (el número son los minutos que le faltan al arbol para quemarse).
    Para cada minuto se actualizan sus celdas y luego se retorna los minutos que duró la simulación.
    Se piden las siguientes variables
    n --> tamaño del bosque
    d --> densidad inicial del bosque
    tq --> tiempo en minutos que tarda un arbol en quemarse por completo
    p --> lista de 8 porcentajes de probabilidad de que un arbol se queme según la cantidad de vecinos quemandose.
    '''
    # Generar la matriz
    matriz = []
    for i in range(n):
        fila = []
        for i in range(n):
            r = random.random()
            if r <= d:
                c = -1
            else:
                c = -2
            fila += [c]
        matriz += [fila]
    t = 1
    # Inicializar las celdas centrales
    mitad = n//2
    for fila in matriz:
        if matriz[mitad-2] == fila or matriz[mitad-1] == fila or matriz[mitad] == fila:
            fila[mitad-2] = tq 
            fila[mitad-1] = tq 
            fila[mitad] = tq 
    # Datos
    total, vacios, quemados, vivos, quemandose, arbolesQuedan = Datos(matriz)
    # === t = ... ===
    # Bucle para que se realize hasta q no haya árboles quemandose
    while quemandose != 0:
        t += 1
        matriz = Actualizar(matriz,p,tq)
        vivos = 0
        for i in matriz:
            vivos +=  i.count(-1)
        quemados = 0
        for i in matriz:
            quemados += i.count(0)
        vacios = 0
        for i in matriz:
            vacios += i.count(-2)
        total = 0
        for i in matriz:
            total += len(i)
        quemandose = total - vacios - quemados - vivos
    return t

# Ejecuto la función en un bucle que realice la simulación 1000 veces y sume el tiempo total 
x = 0
tiempo = 0
repeticiones = 1000
while x < repeticiones:
    t = IncendioTiempo(30, 0.6, 3, [0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1])
    tiempo += t 
    x += 1

# Imprimo el promedio
print(f"El tiempo promedio que dura un incendio en apagarse naturalmente es de {tiempo/repeticiones} minutos")