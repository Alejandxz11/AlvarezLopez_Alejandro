#1 Elabora un programa que solicite al usuario un número entero positivo y, utilizando un ciclo determine si el número ingresado esprimo o no, mostrando el resultado en pantalla
for i in range(1, 11):
    print(i)
num = int(input("Ingresa un número entero positivo: "))
if num > 1:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {num} es primo.")
    else:
        print(f"El número {num} no es primo.")
#2 Desarrolla un programa que pida al usuario una cadena de texto y cuente cuántas vocales consonantes y espacios contiene, mostrando el conteo de cada uno por separado
texto = input("Ingresa una cadena de texto: ")  
vocales = "aeiouAEIOU"
contador_vocales = 0
contador_consonantes = 0
contador_espacios = 0
for char in texto:
    if char in vocales:
        contador_vocales += 1
    elif char.isalpha():
        contador_consonantes += 1
    elif char == " ":
        contador_espacios += 1
print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Espacios: {contador_espacios}")
#3 Crea un programa que solicite al usuario una cantidad indeterminada de números enteros hasta que se ingrese el valor 0, almacenandolos en una lista y mostrando al final el mayor, el menor y la suma total de los numeros capturados
numeros = []  
num = int(input("Ingresa un número entero (0 para terminar): "))
while num != 0:
    numeros.append(num)  
    num = int(input("Ingresa otro número (0 para terminar): "))
if len(numeros) > 0:
    print("Números ingresados:", numeros)
    print("Número mayor:", max(numeros))
    print("Número menor:", min(numeros))
    print("Suma total:", sum(numeros))
else:
    print("No se ingresaron números")
#4 Desarrolla un programa que solicite al usuario una palabra y determine si es un palindromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda
palabra = input("Ingresa una palabra: ")
palabra = palabra.lower()
invertida = palabra[::-1]
if palabra == invertida:
    print("La palabra es un palíndromo")
else:
    print("La palabra NO es un palíndromo")
#5 Crea un programa que pida un numero entero y muestre la tabla de multiplicar de ese número del 1 al 10 
numero = int(input("Ingresa un número entero: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
#6 Crea un programa que solicite "El nombre de un objeto, su color {color} y se utiliza principalmente para {uso}"
objeto = input("Ingresa el nombre del objeto: ")
color = input("Ingresa el color del objeto: ")
uso = input("¿Para qué se utiliza principalmente?: ")
print("El nombre de un objeto es", objeto + ", su color es", color, "y se utiliza principalmente para", uso)
