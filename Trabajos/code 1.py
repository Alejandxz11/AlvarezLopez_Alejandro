# 1Haz un programa que calcule cuántos números del 1 al 100 son divisibles entre 3 y entre 5

count_3 = 0
count_5 = 0

for i in range(1, 101):
    if i % 3 == 0:
        count_3 += 1
    if i % 5 == 0:
        count_5 += 1

print("Números divisibles entre 3:", count_3)
print("Números divisibles entre 5:", count_5)

#2 Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.

positivos = 0
negativos = 0

while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)

#3 Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos.

num = int(input("Ingresa un número: "))

if num % 2 == 0 and num % 3 == 0:
    print("Es divisible entre 2 y 3")
elif num % 2 == 0:
    print("Es divisible entre 2")
elif num % 3 == 0:
    print("Es divisible entre 3")
else:
    print("No es divisible entre 2 ni 3")

#4 Haz un programa que sume todos los números impares del 1 al 50.

suma = 0
for i in range(1, 51):
  if i % 2 == 1:
    suma += i
print("Suma de impares:", suma)

#5 Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría: Menor de 13 años -> "Niño" 13 a 17 años -> "Adolescente" - 18 a 64 años -> "Adulto"- 65 o más -> "Adulto mayor"

edad = int(input("Ingresa la edad: "))

if edad < 13:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")

#6 Haz un programa que pida un número, y muestre si es primo o no.

n = int(input("Ingresa un número: "))
if n < 2:
    print("No es primo")
else:
    es_primo = True
i = 2
while i * i <= n:
    if n % i == 0:
        es_primo = False
    break
i += 1
if es_primo:
    print("Es primo")
else:
    print("No es primo")

#7 Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.

n = int(input("Ingresa un número: "))
suma = 0
i = 1
while i <= n:
    suma += i
i += 1
print("Suma:", suma)

#8 Pide dos números y muestra todos los números entre ellos que sean múltiplos de 7.

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

#9 Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

cantidad = int(input("¿Cuántos productos vas a ingresar?: "))
subtotal = 0.0
i = 1
while i <= cantidad:
    entrada = input("Precio del producto {}: ".format(i))
    try:
        precio = float(entrada.replace(',', '.'))
        if precio < 0:
            print("Precio no puede ser negativo. Intenta de nuevo.")
            continue
    except ValueError:
        print("Entrada inválida. Usa números, por ejemplo 12.50")
        continue
    subtotal += precio
    i += 1
iva = subtotal * 0.16
total = subtotal + iva
print("Subtotal:", round(subtotal, 2))
print("IVA (16%):", round(iva, 2))
print("Total con IVA:", round(total, 2))

#10 Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir.

while True:
    print("----- Calculadora -----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    if opcion == "5":
        print("Saliendo...")
        break
    if opcion in ("1", "2", "3", "4"):
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada inválida. Usa números, intenta de nuevo.")
            continue
        if opcion == "1":
            print("Resultado:", a + b)
        elif opcion == "2":
            print("Resultado:", a - b)
        elif opcion == "3":
            print("Resultado:", a * b)
        elif opcion == "4":
            if b == 0:
                print("Error: división por cero.")
            else:
                print("Resultado:", a / b)
    else:
        print("Opción inválida. Intenta de nuevo.")