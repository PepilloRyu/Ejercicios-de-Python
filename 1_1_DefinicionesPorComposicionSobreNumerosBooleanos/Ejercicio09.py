# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(lista) es la lista formada por el menor y mayor elemento
# de lista.
# rango([3, 2, 7, 5]) == [2, 7]
# ---------------------------------------------------------------------

def rango(lista):
    numeroMenor = min(lista)
    numeroMayor = max(lista)
    print("El numero mayor es:", numeroMayor)
    print("El numero menor es:", numeroMenor)        
    return numeroMayor, numeroMenor

def nuevaLista(numeroMayor, numeroMenor):
    listaNueva = [numeroMenor, numeroMayor]
    print("Lista nueva:", listaNueva)
    return

def pedirLista():
    lista = []
    for i in range(5):
        numero = int(input(f"Numero: {i+1} :"))
        lista.append(numero)
    return lista

def inicializarPrograma():
    lista = pedirLista()
    numeroMayor, numeroMenor = rango(lista)
    nuevaLista(numeroMayor, numeroMenor)
    return

inicializarPrograma()