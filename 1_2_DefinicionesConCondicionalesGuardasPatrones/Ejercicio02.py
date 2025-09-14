# ---------------------------------------------------------------------
# Ejercicio 2. La disyunción excluyente de dos fórmulas se verifica si
# una es verdadera y la otra es falsa. Su tabla de verdad es
# x     | y     | xor x y
# ------+-------+---------
# True  | True  | False
# True  | False | True
# False | True  | True
# False | False | False
#
# Definir la función
# xor : (bool, bool) -> bool
# tal que xor(x, y) es la disyunción excluyente de x e y. Por ejemplo,
# xor(True, True) == False
# xor(True, False) == True
# xor(False, True) == True
# xor(False, False) == False
# ---------------------------------------------------------------------

def xor (x : bool, y : bool) -> bool:
    return x != y

def inicializarPrograma():
    print("Tabla de verdad XOR:")
    print("x     | y     | xor(x, y)")
    print("------+-------+-----------")
    
    casos = [(True,True), (True, False), (False,True), (False,False)]
    for x, y in casos:
        resultado = xor(x, y)
        print(f"{str(x):<6} | {str(y):<6} | {resultado}")
    return

inicializarPrograma()
