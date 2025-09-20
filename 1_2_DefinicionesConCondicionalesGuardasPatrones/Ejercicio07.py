# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# numeroMayor : (int, int) -> int
# tal que numeroMayor(x, y) es el mayor número de dos cifras que puede
# construirse con los dígitos x e y. Por ejemplo,
# numeroMayor(2, 5) == 52
# numeroMayor(5, 2) == 52
# ---------------------------------------------------------------------

def numeroMayor(x,y):
    num1 = int(str(x) + str(y))
    num2 = int(str(y) + str(x))
    return max(num1,num2)
    
def pedirNumeros():
    print("Ingrese 2 numeros : ")
    x = int(input("x : "))
    y = int(input("y : "))
    return x,y

def inicializarPrograma():
    x,y = pedirNumeros()
    resultado = numeroMayor(x,y)
    print("Numero mayor : ",resultado)
    return

inicializarPrograma()