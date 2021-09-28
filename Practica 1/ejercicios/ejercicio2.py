import random
import time

# Algoritmo de seleccion
def ordena_seleccion(m):
    for i in range(len(m)):
        min = i


        for j in range(i, len(m)):
            if m[j] < m[min]:
                min = j

        if min != i:
            m[i], m[min] = m[min], m[i]

# Algoritmo de insercion
def ordena_insercion(m):
    for i in range(len(m)):
        valor = m[i]
        posicion = i

        while posicion > 0 and m[posicion - 1] > valor:
            m[posicion] = m[posicion - 1]
            posicion = posicion - 1

        m[posicion] = valor

inicio_seleccion = time.time()
m = random.sample(range(500), 100)
#print(m)
ordena_seleccion(m)
#print(m)
fin_seleccion = time.time()

inicio_insercion = time.time()
m1 = random.sample(range(500), 100)
#print(m1)
ordena_insercion(m1)
#print(m1)
fin_insercion = time.time()

print("Tiempo del algoritmo de seleccion: " + str(fin_seleccion-inicio_seleccion))
print("Tiempo del algoritmo de insercion: " + str(fin_insercion-inicio_insercion))