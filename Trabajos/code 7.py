#Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.

n = int(input("Ingresa un número: "))
suma = 0
i = 1
while i <= n:
    suma += i
i += 1
print("Suma:", suma)