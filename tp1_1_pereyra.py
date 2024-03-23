import random
from tp1_funciones_pereyra import Datos, aColor, Imprimir, Actualizar

def Incendio(n, d, tq, p):
    '''
    Realiza una simulación de un incendio de un bosque en una matriz con estos valores:
    -2 --> celda vacía.
    -1 --> arbol vivo.
    0 --> arbol quemado.
    numero positivo --> arbol quemandose (el número son los minutos que le faltan al arbol para quemarse).
    Para cada minuto se actualizan sus celdas y luego se imprime el "bosque" y sus datos.
    Se toman las siguientes variables:
    n --> tamaño del bosque
    d --> densidad inicial del bosque
    tq --> tiempo en minutos que tarda un arbol en quemarse por completo
    p --> lista de 8 porcentajes de probabilidad de que un arbol se queme según la cantidad de vecinos
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
    matriz_t0 = [fila[:] for fila in matriz]

    # === t = 0 ===
    t = 0
    # Datos
    total, vacios, quemados, vivos, quemandose, arbolesQuedan = Datos(matriz)
    
    # Cambiar los números por colores
    matriz_t0 = aColor(matriz_t0)
    
    # Imprimir 
    Imprimir(matriz_t0, 0, quemandose, arbolesQuedan, quemados)
    
    # === t = 1 ===
    t = 1

    # Inicializar las celdas centrales
    mitad = n//2
    for fila in matriz:
        if matriz[mitad-2] == fila or matriz[mitad-1] == fila or matriz[mitad] == fila:
            fila[mitad-2] = tq 
            fila[mitad-1] = tq 
            fila[mitad] = tq 
    matriz_t1 = [fila[:] for fila in matriz] 
    
    # Datos
    total, vacios, quemados, vivos, quemandose, arbolesQuedan = Datos(matriz)
    
    # Cambiar los números por colores
    matriz_t1 = aColor(matriz_t1)
    
    # Imprimir 
    Imprimir(matriz_t1, 1, quemandose, arbolesQuedan, quemados)

    # === t = ... ===
    # Bucle para que se realize hasta q no haya árboles quemandose
    while quemandose != 0:
            t += 1
            matriz = Actualizar(matriz,p,tq)
            matriz_color = [fila[:] for fila in matriz]
            matriz_color = aColor(matriz_color)
            # Datos
            total, vacios, quemados, vivos, quemandose, arbolesQuedan = Datos(matriz)
            Imprimir(matriz_color, t, quemandose, arbolesQuedan, quemados)

# Ejecuto la función con los valores dados para esta parte del tp
Incendio(30, 0.6, 3, [0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1])