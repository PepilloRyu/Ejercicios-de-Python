# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# numeroDeRaices : (float, float, float) -> float
# tal que numeroDeRaices(a, b, c) es el número de raíces reales de la
# ecuación a*x^2 + b*x + c = 0. Por ejemplo,
# numeroDeRaices(2, 0, 3) == 0
# numeroDeRaices(4, 4, 1) == 1
# numeroDeRaices(5, 23, 12) == 2
# ---------------------------------------------------------------------

def numeroRaices(a,b,c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        return 2
    elif discriminante == 0:
        return 1
    else:
        return 0

def ingresarConstantes():
    print("Ingrese las constantes siguientes :")
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))
    return a,b,c

def inicializarPrograma():
    a,b,c = ingresarConstantes()
    resultado = numeroRaices(a,b,c)
    print(f"\nPara la ecuación {a}x² + {b}x + {c} = 0")
    print(f"Número de raíces reales: {resultado}")
    return

inicializarPrograma()