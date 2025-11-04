# Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if a > b:
    a, b = b, a
encontrado = False
for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
encontrado = True
if not encontrado:
        print("No hay múltiplos de 7 en el rango")