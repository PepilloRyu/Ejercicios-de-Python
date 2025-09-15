# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p) es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
# intercambia((2,5)) == (5,2)
# intercambia((5,2)) == (2,5)
# ---------------------------------------------------------------------

def intercambia(tupla):
    tuplaInvertida = tupla[::-1]
    return tuplaInvertida

def inicializarPrograma():
    tupla = ('A' , 'B')
    print("Tupla original : ", tupla)
    resultado = intercambia(tupla)
    print("Tupla intercambiada : ",resultado)
    return

inicializarPrograma()