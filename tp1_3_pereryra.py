import random
from tp1_funciones_pereyra import Actualizar, Datos

def IncendioDensidades(n, d, tq, p):
    '''
    Realiza una simulación de un incendio de un bosque en una matriz con estos valores:
    -2 --> celda vacía.
    -1 --> arbol vivo.
    0 --> arbol quemado.
    numero positivo --> arbol quemandose (el número son los minutos que le faltan al arbol para quemarse).
    Para cada minuto se actualizan sus celdas y luego se retorna la cantidad de árboles vivos y cantidad de arboles quemados.
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
        arbolesTotal = total - vacios 
    return arbolesTotal, quemados


print(f"+----------+----------------+\n| Densidad | Bosque quemado |")
densidades = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
esp = " "
for d in densidades:
    x = 0
    arboles = 0
    quemados = 0
    while x < 100:
        a, b = IncendioDensidades(30, d, 3, [0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1])
        arboles += a
        quemados += b
        x += 1
        porcentaje = quemados*100/arboles
        porcentajeRound = str(round(porcentaje, 2))
    print(f"+----------+----------------+\n| {d}{esp*5} | {porcentajeRound} % {esp*(12 - len(porcentajeRound))}|")
print("+----------+----------------+")