# ---------------------------------------------------------------------
# Ejercicio 13. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
# ---------------------------------------------------------------------

def segmento(m, n, xs):
    if m > n:
        return []
    return xs[m:n+1]

def pedirIndices():
    while True:
        try:
            print("Ingrese el índice m:")
            m = int(input("m: "))
            print("Ingrese el índice n:")
            n = int(input("n: "))
            return m, n
        except ValueError:
            print("ERROR: Debe ingresar números enteros válidos")

def pedirLista():
    lista = []
    print("Ingrese los números de la lista (termine con 'fin')")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("ERROR: La entrada no es válida")
    return lista

def inicializarPrograma():
    lista = pedirLista()
    print(f"Lista creada: {lista}")
    
    m, n = pedirIndices()
    resultado = segmento(m, n, lista)
    
    print(f"segmento({m}, {n}, {lista}) == {resultado}")

inicializarPrograma()