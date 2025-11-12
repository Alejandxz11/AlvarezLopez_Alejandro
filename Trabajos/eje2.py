# Ejercicio 5 Haz un programa que pida un número, y crea una nueva lista sin duplicados. Pide 10 números.
lista_numeros = []
for i in range(10):
    numero = input("Ingresa un número: ")
    lista_numeros.append(numero)
lista_sin_duplicados = list(set(lista_numeros))
print("Lista sin duplicados:", lista_sin_duplicados)
# 