# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# divisionSegura : (float, float) -> float
# tal que divisionSegura(x, y) es x/y si y no es cero y 9999 en caso
# contrario. Por ejemplo,
# divisionSegura(7, 2) == 3.5
# divisionSegura(7, 0) == 9999.0
# ---------------------------------------------------------------------

def divisionSegura(x,y):
    if y == 0:
        return 9999.0
    else : 
        resultado = x/y
    return resultado

def inicializarPrograma():
    print("Ingrese 2 números float")
    x = float(input("x : "))
    y = float(input("y : "))
    resultado = divisionSegura(x,y)
    print("Resultado : ", resultado)
    return

inicializarPrograma()