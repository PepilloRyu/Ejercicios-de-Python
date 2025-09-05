# ---------------------------------------------------------------------
# Ejercicio 15. Definir la función
# mediano : (int, int, int) -> int
# tal que mediano(x, y, z) es el número mediano de los tres números x, y
# y z. Por ejemplo,
# mediano(3, 2, 5) == 3
# mediano(2, 4, 5) == 4
# mediano(2, 6, 5) == 5
# mediano(2, 6, 6) == 6
# ---------------------------------------------------------------------

def mediano(x,y,z):
    numOrdenados = sorted([x,y,z])
    print("Mediano : ", numOrdenados[1])
    return 

def pedirNumeros():
    print("Ingrese los numeros")
    x = int(input("x : "))
    y = int(input("y : "))
    z = int(input("z : "))
    return x,y,z

def inicializarPrograma():
    x,y,z = pedirNumeros()
    mediano(x,y,z)
    return

inicializarPrograma()