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