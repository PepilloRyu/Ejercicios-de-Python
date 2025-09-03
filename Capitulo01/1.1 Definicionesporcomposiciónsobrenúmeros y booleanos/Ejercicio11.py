# ---------------------------------------------------------------------
# Ejercicio 11. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]
# ---------------------------------------------------------------------

def interior(lista):
    if len(lista) < 2:
        print("La lista necesita almenos 2 numeros")
        return
    
    primerElemento = lista.pop(0)
    ultimoElemento = lista.pop()
    print("Primer elemento",primerElemento)
    print("Ultimo elemento", ultimoElemento)
    print("Lista sin los elementos", lista)
    return 

def ingresarLista():
    lista = []
    
    while(True):
        entrada = input("Numero: ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print(f"¡Ups! '{entrada}' no es un número válido. Intenta de nuevo.")      
    return lista

def inicializarPrograma():
    lista = ingresarLista()
    interior(lista)
    
    return

inicializarPrograma()