#---------------------------------------------------------------------
# Ejercicio 12. Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
# ---------------------------------------------------------------------

def finales(lista, ultimosNumeros):
    print(f"Lista con los ultimos {ultimosNumeros} es {lista}")
    return

def pedirLista(numero):
    lista = []
    
    for i in range(numero):
        numero = int(input(f"Numero para la lista {i+1}:"))
        lista.append(numero)
    
    return lista

def pedirTamañoLista():
    print("Ingrese el tamaño de la lista")
    tamLista = int(input("Tamaño : "))
    return tamLista

def pedirUltimosDigitosAMostrar(tamLista):
    print("Ingrese la cantidad de numeros que quiere mostrar : ")
    while True:
        ultimosNumeros= int(input("Numero : "))
        if tamLista > ultimosNumeros :
            print("El tamaño de la lista debe ser mayor o igual que los numeros a mostrar")
    
            
    return ultimosNumeros

def inicializarPrograma():
    tamLista = pedirTamañoLista()
    ultimosNumeros = pedirUltimosDigitosAMostrar(tamLista)
    lista = pedirLista(tamLista)
    finales(lista, ultimosNumeros)
    return

inicializarPrograma()
