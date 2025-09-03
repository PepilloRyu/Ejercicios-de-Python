# ---------------------------------------------------------------------
# Ejercicio 11. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]
# ---------------------------------------------------------------------

def interior(lista):
    if len(lista) <= 2:
        return []
    return lista[1:-1]

def finales(n, xs):
    return xs[-n:]

def pedirLista(tamano):
    lista = []
    for i in range(tamano):
        while True:
            try:
                num = int(input(f"Número {i+1} de {tamano}: "))
                lista.append(num)
                break
            except ValueError:
                print("Error: Ingrese un número válido")
    return lista

def pedirTamañoLista():
    while True:
        try:
            tamLista = int(input("Tamaño de la lista: "))
            if tamLista >= 0:
                return tamLista
            print("Error: El tamaño debe ser >= 0")
        except ValueError:
            print("Error: Ingrese un número válido")

def pedirUltimosDigitosAMostrar(tamLista):
    while True:
        try:
            ultimosNumeros = int(input("Elementos a mostrar: "))
            if 0 <= ultimosNumeros <= tamLista:
                return ultimosNumeros
            print(f"Error: Debe ser entre 0 y {tamLista}")
        except ValueError:
            print("Error: Ingrese un número válido")

def inicializarPrograma():
    tamLista = pedirTamañoLista()
    lista = pedirLista(tamLista)
    
    resultado_interior = interior(lista)
    print(f"Interior de la lista: {resultado_interior}")
    
    if tamLista > 0:
        ultimosNumeros = pedirUltimosDigitosAMostrar(tamLista)
        resultado_finales = finales(ultimosNumeros, lista)
        print(f"Últimos {ultimosNumeros} elementos: {resultado_finales}")

inicializarPrograma()