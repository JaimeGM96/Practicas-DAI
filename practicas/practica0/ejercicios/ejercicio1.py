from random import randint

numero_a_adivinar = randint(1, 100)
numero_introducido = 101

while numero_a_adivinar != numero_introducido :
    numero_introducido = int(input("Introduce el numero que crees que es: "))
    
    if numero_a_adivinar > numero_introducido :
        print("El número buscado es mayor.")
    elif numero_a_adivinar < numero_introducido :
        print("El número buscado es menor.")

print("Has acertado!")