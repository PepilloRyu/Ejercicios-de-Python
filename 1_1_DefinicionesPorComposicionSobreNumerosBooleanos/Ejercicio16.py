# ---------------------------------------------------------------------
# Ejercicio 16. Definir la función
# tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False
# ---------------------------------------------------------------------


def tresIguales(x,y,z):
    if x and y and z == x and y and z:
        print("Son iguales")
        return
    else:
        print("Son diferentes")
        return


def inicializarPrograma():
    print("Ingrese x,y,z")
    x = int(input("x : "));
    y = int(input("y : "));
    z = int(input("z : "));
    tresIguales(x,y,z)
    return

inicializarPrograma()