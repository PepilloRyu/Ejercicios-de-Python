# ---------------------------------------------------------------------
# Ejercicio 14. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos es la lista formada por los primeros
# elementos y los finales elementos. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]
# --------------------------------------------------------------------

def extremos(lista, extremo):
    if extremo <= 0:
        return []
    if 2 * extremo >= len(lista):
        return lista
    return lista[:extremo] + lista[-extremo:]

def pedirextremos():
    print("Ingrese el extremo")
    extremo = int(input("Extremo:"))
    return extremo

def inicializarPrograma():
    lista = [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]
    print("Lista:", lista)
    extremo = pedirextremos()
    extremos(lista, extremo)
    lista[extremo:-extremo] = extremos(lista, extremo)
    print("Lista sin extremos:", lista[extremo:-extremo])
    return

inicializarPrograma()