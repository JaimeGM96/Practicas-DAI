# Fibonacci
def fibonacci(n):
    n0 = 0
    n1 = n2 = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        i = 3
        while i != n+1:
            n2 = n0 + n1
            n0, n1 = n1, n2
            i += 1

        return n2


f = open("entrada.txt")
n = f.read()
n = int(n)
f.close()

resultado = fibonacci(n)

f = open("salida.txt", "w")
f.write(str(resultado))
f.close()