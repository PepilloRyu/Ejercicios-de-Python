# ---------------------------------------------------------------------
# Ejercicio 6. Definir una función
# ciclo : (list[A]) -> list[A]
# tal que ciclo(xs) es la lista obtenida permutando cíclicamente los
# elementos de la lista xs, pasando el último elemento al principio de
# la lista. Por ejemplo,
# ciclo([2, 5, 7, 9]) == [9, 2, 5, 7]

# ---------------------------------------------------------------------

def ciclo(lista):
    elemento = lista.pop()
    print("Lista sin ultimo elemento : ",lista)
    lista.insert(0,elemento)
    return lista

def inicializarPrograma():
    lista = [2, 5, 7, 9]
    print("Lista original : ", lista)
    lista = ciclo(lista)
    print("Lista nueva : ",lista)
    return

inicializarPrograma()