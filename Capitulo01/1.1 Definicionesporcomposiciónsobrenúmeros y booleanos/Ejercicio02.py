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

def sumarMonedas(cant_a: int, cant_b: int, cant_c: int, cant_d: int, cant_e: int) -> float:
    valor_a = 1
    valor_b = 2
    valor_c = 5
    valor_d = 10
    valor_e = 20
    
    total = (cant_a * valor_a) + (cant_b * valor_b) + (cant_c * valor_c) + (cant_d * valor_d) + (cant_e * valor_e)
    
    return total

def pedirMonedas():
    print("Ingrese cuantas monedas tiene de 1:")
    cant_a = int(input("a:"))
    print("Ingrese cuantas monedas tiene de 2:")
    cant_b = int(input("b:"))
    print("Ingrese cuantas monedas tiene de 5:")
    cant_c = int(input("c:"))
    print("Ingrese cuantas monedas tiene de 10:")
    cant_d = int(input("d:"))
    print("Ingrese cuantas monedas tiene de 20:")
    cant_e = int(input("e:"))
    return cant_a, cant_b, cant_c, cant_d, cant_e

def inicializarPrograma():
    cant_a, cant_b, cant_c, cant_d, cant_e = pedirMonedas()
    total = sumarMonedas(cant_a, cant_b, cant_c, cant_d, cant_e)
    print(f"Tiene:" , total)
    return


inicializarPrograma()