# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# rota : (int, List[A]) -> List[A]
# tal que rota(vecesRotada, lista) es la lista obtenida poniendo los vecesRotada primeros
# elementos de lista al final de la lista. Por ejemplo,
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
# ---------------------------------------------------------------------

def rotar(lista, vecesRotada):
    for i in range(vecesRotada):
        if len(lista) > 1:
            primerElemento = lista.pop(0)
            lista.append(primerElemento) 
        print("Lista rotada:", lista)
    return

def pedirNumeros():
    lista = []
    for i in range(4):
        numero = int(input(f"Numero: {i+1} :"))
        lista.append(numero)
        
    print("La lista es :", lista)
    
    print("Cuantas veces debe rotar?")
    vecesRotada = int(input("Num:"))
    return lista, vecesRotada

def inicializarPrograma():
    lista, vecesRotada = pedirNumeros()
    rotar(lista, vecesRotada)
    return

inicializarPrograma()