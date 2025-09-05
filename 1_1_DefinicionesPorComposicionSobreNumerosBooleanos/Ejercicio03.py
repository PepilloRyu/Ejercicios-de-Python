# ---------------------------------------------------------------------
# Ejercicio 3. Definir la función
# volumenEsfera : (float) -> float
# tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
# ejemplo,
# volumenEsfera(10) == 4188.790204786391
# ---------------------------------------------------------------------
from math import pi

def volumenEsfera(radio:float) -> float:
    volumen = (4/3) * pi * radio ** 3
    return volumen

def pedirRadio() -> float:
    print("Ingrese el radio")
    return float(input())

def inicializarPrograma():
    radio = pedirRadio()
    resultado = volumenEsfera(radio)
    print(f"El volumen de la esfera con radio {radio} es: {resultado}")
    return

inicializarPrograma()

