#---------------------------------------------------------------------
# Ejercicio 12. Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales es la lista formada por los n finales
# elementos. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
# ---------------------------------------------------------------------

def finales(n, xs):
    return xs[-n:]

def pedirLista(tamano):
    lista = []
    for i in range(tamano):
        num = int(input(f"Numero {i+1} de {tamano}: "))
        lista.append(num)
    return lista

def pedirTamañoLista():
    tamLista = int(input("Tamaño de la lista: "))
    return tamLista

def pedirUltimosDigitosAMostrar(tamLista):
    while True:
        ultimosNumeros = int(input("Elementos a mostrar: "))
        if ultimosNumeros <= tamLista:
            return ultimosNumeros
        print("Error: La cantidad debe ser <= al tamaño de la lista")

def inicializarPrograma():
    tamLista = pedirTamañoLista()
    ultimosNumeros = pedirUltimosDigitosAMostrar(tamLista)
    lista = pedirLista(tamLista)
    resultado = finales(ultimosNumeros, lista)
    print(f"Ultimos {ultimosNumeros} elementos: {resultado}")

inicializarPrograma()
