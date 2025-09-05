# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
# rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
# rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------

def rota1(listaA):
    if len(listaA) <= 1:
        return listaA
    return listaA[1:] + [listaA[0]]

def ingresarLista():
    print("Ingrese 5 numeros")
    listaA = []
    for i in range(5):
        numero = int(input(f"Numero {i+1} : "))
        listaA.append(numero)

    print("La lista de numeros es:", listaA)
    return listaA

def inicializarPrograma():
    listaA = ingresarLista()
    listaRotada = rota1(listaA)
    print("Lista rotada", listaRotada)
    return

inicializarPrograma()