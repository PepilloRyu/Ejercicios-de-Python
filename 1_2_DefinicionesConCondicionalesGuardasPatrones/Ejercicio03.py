# ---------------------------------------------------------------------
# Ejercicio 3. Las dimensiones de los rectángulos puede representarse
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
# altura 3.
#
# Definir la función
# mayorRectangulo : (tuple[float, float], tuple[float, float])
# -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
# mayorRectangulo((4, 6), (3, 7)) == (4, 6)
# mayorRectangulo((4, 6), (3, 8)) == (4, 6)
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)
# ---------------------------------------------------------------------

def mayorRectangulo(primerTupla, segundaTupla):
    areaPrimerRectangulo = primerTupla[0] * primerTupla[1]
    print("Area 1ro : ", areaPrimerRectangulo) 
    
    areaSegundoRectangulo = segundaTupla[0] * segundaTupla[1]
    print("Area 2do : ", areaSegundoRectangulo)
    
    if areaPrimerRectangulo > areaSegundoRectangulo:
        print("El primer rectangulo tiene mayor area")
        return primerTupla
    elif areaPrimerRectangulo < areaSegundoRectangulo:
        print("El segundo rectangulo tiene mayor area")
        return segundaTupla
    else:
        print("Tienen la misma area")
        return primerTupla

def pedirRectangulo(numero):
    while True:
        print(f"---{numero} rectángulo---")
        
        try:
            base = float(input("Base: "))
            if base <= 0:
                print("Error: La base debe ser mayor a 0")
                continue
            
            altura = float(input("Altura: "))
            if altura <= 0:
                print("Error: La altura debe ser mayor a 0")
                continue
            
            rectangulo = (base, altura)
            print(f"Rectángulo creado: {rectangulo}")
            return rectangulo
            
        except ValueError:
            print("ERROR: Ingrese un valor válido")

def inicializarPrograma():
    primerTupla = pedirRectangulo("1er")
    segundaTupla = pedirRectangulo("2do")
    
    resultado = mayorRectangulo(primerTupla, segundaTupla)
    print(f"El rectángulo con mayor área es: {resultado}")
    
    return

inicializarPrograma()