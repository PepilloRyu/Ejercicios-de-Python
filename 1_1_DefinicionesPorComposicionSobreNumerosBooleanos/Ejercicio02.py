# ---------------------------------------------------------------------
# Ejercicio 2. Definir la función
# sumaMonedas : (int, int, int, int, int) -> int
# tal que sumaMonedas(a, b, c, d, e) es la suma de los euros
# correspondientes a a monedas de 1 euro, b de 2 euros, c de 5 euros, d
# 10 euros y e de 20 euros. Por ejemplo,
# sumaMonedas(0, 0, 0, 0, 1) == 20
# sumaMonedas(0, 0, 8, 0, 3) == 100
# sumaMonedas(1, 1, 1, 1, 1) == 38
# ---------------------------------------------------------------------

def sumarMonedas(cantidadA: int, cantidadB: int, cantidadC: int, cantidadD: int, cantidadE: int) -> int:
    valorA = 1
    valorB = 2
    valorC = 5
    valorD = 10
    valorE = 20
    total = (cantidadA * valorA) + (cantidadB * valorB) + (cantidadC * valorC) + (cantidadD * valorD) + (cantidadE * valorE)
    return total

def pedirMonedas():
    print("Ingrese cuantas monedas tiene de 1:")
    cantidadA = int(input("a:"))
    print("Ingrese cuantas monedas tiene de 2:")
    cantidadB = int(input("b:"))
    print("Ingrese cuantas monedas tiene de 5:")
    cantidadC = int(input("c:"))
    print("Ingrese cuantas monedas tiene de 10:")
    cantidadD = int(input("d:"))
    print("Ingrese cuantas monedas tiene de 20:")
    cantidadE = int(input("e:"))
    return cantidadA, cantidadB, cantidadC, cantidadD, cantidadE

def inicializarPrograma():
    cantidadA, cantidadB, cantidadC, cantidadD, cantidadE = pedirMonedas()
    total = sumarMonedas(cantidadA, cantidadB, cantidadC, cantidadD, cantidadE)
    print(f"Tiene:" , total)
    return


inicializarPrograma()