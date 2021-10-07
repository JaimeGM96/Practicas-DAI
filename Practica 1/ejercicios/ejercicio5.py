import random

def generar_cadena(n):
    cadena = ''

    for i in range(n):
        aleatorio = random.randint(0, 1)
        if aleatorio == 0:
            cadena = cadena + "["
        else:
            cadena = cadena + "]"

    return cadena

def validar_cadena(cadena):
    valida = False

    for i in range(len(cadena)):
        print(cadena[i])

    return valida

longitud_cadena = random.randint(1, 10)
cadena = generar_cadena(longitud_cadena)
es_valida = validar_cadena(cadena)

if es_valida:
    print("La cadena " + cadena + " es valida")
else:
    print("La cadena " + cadena + " no es valida")