# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# areaDeCoronaCircular : (float, float) -> float
# tal que areaDeCoronaCircular(r1, r2) es el área de una corona
# circular de radio interior r1 y radio exterior r2.
# ---------------------------------------------------------------------
from math import pi

def areaDeCoronaCircular(radioMayor: float, radioMenor: float) -> None:
    areaMayor = pi * radioMayor **2
    areaMenor = pi * radioMenor **2
    areaCorona = areaMayor - areaMenor
    print(f"El area de la corona es de :{areaCorona:.2f} ")
    return

def introducirRadios() -> tuple[float, float]:
    print("Ingrese el valor del radio mayor:")
    radioMayor = float(input("Radio mayor:"))
    
    print("Ingrese el valor del radio menor:")
    radioMenor = float(input("Radio menor:"))
    return radioMayor, radioMenor

def inicializarPrograma():
    radioMayor, radioMenor =introducirRadios()
    areaDeCoronaCircular(radioMayor, radioMenor)
    return

inicializarPrograma()


