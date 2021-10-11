import re

def validar_palabra(cadena):
    valida = re.search('.+\s+[A-Z]{1}', cadena)

    return valida

def validar_correo(cadena):
    valida = re.search('.+@\w+\.\w+', cadena)

    return valida

def validar_tarjeta_credito(cadena):
    valida = re.search('\d{4}-|\s+\d{4}-|\s+\d{4}-|\s+\d{4}', cadena)

    return valida

cadena = input("Introduce una cadena para ver si es válida: ")

if validar_palabra(cadena) or validar_correo(cadena) or validar_tarjeta_credito(cadena):
    print("La cadena " + cadena + " es válida")
else:
    print("La cadena " + cadena + " no es válida")