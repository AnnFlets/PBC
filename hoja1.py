print("===== Programa para hacer triángulos =====")
print()
print("Ingrese un número entero positivo: " )
numero = int(input())
i = 0
j = 0
print()
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")
print()
print("Programa 1 terminado")
print()
print("===== Programa para determinar números primos =====")
print()
print("Ingrese un número entero positivo: ")
numero2 = int(input())
print()
if numero2 % 2 == 0:
    print("El número ", numero2, " no es primo")
elif numero2 % 3 == 0:
    print("El número ", numero2, " no es primo")
elif numero2 % 5 == 0:
    print("El número ", numero2, " no es primo")
elif numero2 % 7 == 0:
    print("El número ", numero2, " no es primo")
else:
    print("El número ", numero2, " es primo")
print()
print("Programa 2 terminado")
