#Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.

num = int(input("Ingresa un número: "))

if num % 2 == 0 and num % 3 == 0:
    print("Es divisible entre 2 y 3")
elif num % 2 == 0:
    print("Es divisible entre 2")
elif num % 3 == 0:
    print("Es divisible entre 3")
else:
    print("No es divisible entre 2 ni 3")