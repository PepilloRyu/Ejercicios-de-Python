# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# raices : (float, float, float) -> list[float]
# tal que raices(a, b, c) es la lista de las raíces reales de la
# ecuación ax^2 + bx + c = 0. Por ejemplo,
# raices(1, 3, 2) == [-1.0,-2.0]
# raices(1, (-2), 1) == [1.0,1.0]
# raices(1, 0, 1) == []
# --------------------------------------------------------------------
from math import sqrt
def raices (a,b,c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + sqrt(discriminante)) / (2*a)
        x2 = (-b - sqrt(discriminante)) / (2*a)
        return [x1, x2]
    
    elif discriminante == 0:
        x = -b / (2*a)
        return [x, x]      
    else:
        return []

def pedirConstantes():
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))
    return a,b,c

def inicializarPrograma():
    a,b,c = pedirConstantes()
    resultado = raices(a,b,c)
    print(f"\nRaices de {a}x^2 + {b}x + c = 0")
    print("Resultado : ", resultado)
    return

inicializarPrograma()