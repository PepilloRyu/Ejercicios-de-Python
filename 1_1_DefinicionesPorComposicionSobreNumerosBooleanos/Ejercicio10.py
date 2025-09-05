# ---------------------------------------------------------------------
# Ejercicio 10. Definir la función
# palindromo : (List[A])
# tal que palindromo se verifica si es un palíndromo; es decir,
# es lo mismo leer de izquierda a derecha que de derecha a
# izquierda. Por ejemplo,
# palindromo([3, 2, 5, 2, 3]) == True
# palindromo([3, 2, 5, 6, 2, 3]) == False
# ---------------------------------------------------------------------

def palindromo(lista):
    for i in range(len(lista)//2):
        primerElemento = lista[i]
        ultimoElemento = lista[-i-1]
    if primerElemento != ultimoElemento:
        return False
    return True
        

def ingresarLista():
    lista = [1,2,3,3,2,1]
    return lista

def inicializarPrograma():
    lista = ingresarLista()
    if palindromo(lista):
        print("Es un palindromo")
    else:
        print("No es un palindromo")
    return

inicializarPrograma()