# ---------------------------------------------------------------------
# Ejercicio 18. Definir la función
# cuatroIguales : (int, int, int, int) -> bool
# tal que cuatroIguales(x,y,z,u) se verifica si los elementos x, y, z y
# u son iguales. Por ejemplo,
# cuatroIguales(5, 5, 5, 5) == True
# cuatroIguales(5, 5, 4, 5) == False
# ---------------------------------------------------------------------

def cuatroIguales(w,x,y,z) -> bool:
    if w == x == y == z:
        print("Iguales")
        return True
    else :
        print("Diferentes")
    return False

def inicializarPrograma():
    print("Ingrese 4 números ")
    w = int(input("w : "))
    x = int(input("x : "))
    y = int(input("y : "))
    z = int(input("z : "))
    cuatroIguales(w,x,y,z)
    return

inicializarPrograma()