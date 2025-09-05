# ---------------------------------------------------------------------
# Ejercicio 6. Definir la función
# maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
# maxTres(6, 2, 4) == 6
# maxTres(6, 7, 4) == 7
# maxTres(6, 7, 9) == 9
# ---------------------------------------------------------------------

def maxTres(x: int, y: int, z: int) -> int:
    maximo = max(x,y,z)  
    return maximo
    
def pedirNumeros():
    print("Ingrese los")
    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:"))
    return x,y,z

def inicializarPrograma():    
    x,y,z = pedirNumeros()
    maximo = maxTres(x,y,z)
    print("El maximo es:", maximo)
    return

inicializarPrograma()