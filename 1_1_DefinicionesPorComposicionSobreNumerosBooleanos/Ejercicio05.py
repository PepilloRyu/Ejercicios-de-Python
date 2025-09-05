# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# ultimoDigito : (int) -> int
# tal que ultimoDigito(x) es el último dígito del número x. Por
# ejemplo,
# ultimoDigito(325) == 5
# ---------------------------------------------------------------------

def saberUltimoDigito(numero: int) -> int:
    ultimoDigito = abs(numero) % 10
    return ultimoDigito

def pedirNumero():
    print("Ingrese un número:")
    numero = int(input("x:"))
    return numero

def inicializarPrograma():
    numero = pedirNumero()
    ultimoDigito = saberUltimoDigito(numero)
    print(f"Ultimo digito de {numero} es {ultimoDigito}")
    return

inicializarPrograma()