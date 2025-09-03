# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmética de los números x, y y
# z. Por ejemplo,
# media3(1, 3, 8) == 4.0
# media3(-1, 0, 7) == 2.0
# media3(-3, 0, 3) == 0.0
# ---------------------------------------------------------------------

def media3(x: float, y: float, z: float) -> float :  
    resultado = (x+y+z)/3
    return resultado

def introducirNumeros():
    print("Ingrese x, y, z, separados por enter")
    x = float(input("x:"))
    y = float(input("y:"))
    z = float(input("z:"))
    return x, y, z

def inicializarPrograma():
    x, y, z = introducirNumeros()
    resultado = media3(x,y,z)
    
    print(f"El resultado de la media de {x}, {y}, {z} es:,{resultado:.2f}")
    return

inicializarPrograma()