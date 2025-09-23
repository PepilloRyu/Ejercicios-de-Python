# ---------------------------------------------------------------------
# Ejercicio 10. La fórmula de Herón, descubierta por Herón de
# Alejandría, dice que el área de un triángulo cuyo lados miden a, b y c
# es la raíz cuadrada de s(s-a)(s-b)(s-c) donde s es el semiperímetro
# s = (a+b+c)/2
#
# Definir la función
# area : (float, float, float) -> float
# tal que area(a, b, c) es el área del triángulo de lados a, b y c. Por
# ejemplo,
# area(3, 4, 5) == 6.0
# ---------------------------------------------------------------------
from math import sqrt
def calcularArea(s, a,b,c):
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def calcularSemiperimetro(a,b,c):
    s = (a + b + c) / 2
    return s

def ingresarLados():
    print("Ingrese los lados : ")
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))
    return a,b,c

def inicializarPrograma():
    a,b,c = ingresarLados()
    s = calcularSemiperimetro(a,b,c)
    area = calcularArea(s,a,b,c)
    print(f"El area es de : {area:.2f}")
    return

inicializarPrograma()