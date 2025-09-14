# ---------------------------------------------------------------------
# Ejercicio 17. Definir la función
# tresDiferentes : (int, int, int) -> bool
# tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
# son distintos. Por ejemplo,
# tresDiferentes(3, 5, 2) == True
# tresDiferentes(3, 5, 3) == False
# ---------------------------------------------------------------------

def tresDiferentes(x,y,z) -> bool:
    if x != y and x != z and y != z:
        print("Diferentes")
        return True
    else : 
        print("Almenos dos son iguales")
        return False

def inicializarPrograma():
    print("Ingrese 3 números ")
    x = int(input("x : "))
    y = int(input("y : "))
    z = int(input("z : "))
    tresDiferentes(x,y,z)
    return

inicializarPrograma()