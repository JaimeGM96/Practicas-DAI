import re

def validar_palabra(cadena):
    valida = False

    expresion = re.search(r'', cadena)

    return valida

def validar_correo(cadena):
    valida = False

    expresion = re.search(r'', cadena)

    return valida

def validar_tarjeta_credito(cadena):
    valida = False

    expresion = re.search(r'', cadena)

    return valida

cadena = input("Introduce una cadena para ver si es válida: ")

if validar_palabra(cadena) or validar_correo(cadena) or validar_tarjeta_credito(cadena):
    print("La cadena " + cadena + " es válida")
else:
    print("La cadena " + cadena + " no es válida")