# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# distancia : (tuple[float, float], tuple[float, float]) -> float
# tal que distancia(p1, p2) es la distancia entre los puntos p1 y
# p2. Por ejemplo,
# distancia((1, 2), (4, 6)) == 5.0
# ---------------------------------------------------------------------
from math import sqrt

def distancia(tuplaUno, tuplaDos):
    distanciaX = tuplaUno[0] - tuplaDos[0]
    distanciaY = tuplaUno[1] - tuplaDos[1]
    return sqrt(distanciaX ** 2 + distanciaY ** 2)

def pedirPs():
    print("Coordenada 1")
    print("Ingrese p1 y p2 ")
    print("________________")
    p1 = int(input("p1 : "))
    p2 = int(input("p2 : "))
    tuplaUno = (p1,p2)
    
    print("\n\nCoordenada 2")
    print("Ingrese p3 y p4 ")
    print("________________")
    p3 = int(input("p3 : "))
    p4 = int(input("p4 : "))
    tuplaDos = (p3,p4)
    
    return tuplaUno, tuplaDos

def inicializarPrograma():
    tuplaUno,tuplaDos = pedirPs()
    distanciaFinal = distancia(tuplaUno, tuplaDos)
    print("______________")
    print("Distancia : ",distanciaFinal)
    return

inicializarPrograma()