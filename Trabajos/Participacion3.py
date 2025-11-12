#Ejercicio 1 Pide nombres hasta que el usuario escriba la palabra "Fin".Al final muestra cuántos nombres ingresó, y cuál es el primero y el último.

def main():
    nombres = []
    print("Ingrese nombres. Escriba 'Fin' cuando quiera terminar.")
    while True:
        nombre = input("Nombre: ")
        if nombre.strip().lower() == "fin":
            break
        nombres.append(nombre.strip())
    cantidad = len(nombres)
    if cantidad == 0:
        print("\nNo ingresaste ningún nombre.")
    else:
        print(f"\nIngresaste {cantidad} nombre(s).")
        print(f"Primero: {nombres[0]}")
        print(f"Último: {nombres[-1]}")
if __name__ == "__main__":
    main()

# Ejercicio 2 Pide números hasta que el usuario escriba 0. Guarda los pares en una lista y los impares en otra. Al final, muestra cuantos números hay en cada lista. Ordena la lista en orden ascendente y recorre las listas para mostrar cada número uno por uno.

def main():
    lista_pares = []
    lista_impares = []
    print("Ingrese números. Escriba '0' cuando quiera terminar.")
    while True:
        try:
            numero = int(input("Número: "))
            if numero == 0:
                break
            if numero % 2 == 0:
                lista_pares.append(numero)
            else:
                lista_impares.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    print(f"\nCantidad de números pares: {len(lista_pares)}")
    print(f"Cantidad de números impares: {len(lista_impares)}")
    
    lista_pares.sort()
    lista_impares.sort() 
    print("\nNúmeros pares en orden ascendente:")
    for num in lista_pares:
        print(num)
    print("\nNúmeros impares en orden ascendente:")
    for num in lista_impares:
        print(num)
if __name__ == "__main__":
    main()

# Ejercicio 4 Pide una frase y cuenta cuántas vocales usa (a, e, i, o, u).
def contar_vocales(frase):
    a = frase.lower().count('a')
    e = frase.lower().count('e')
    i = frase.lower().count('i')
    o = frase.lower().count('o')
    u = frase.lower().count('u')
    total_vocales = a + e + i + o + u
    return total_vocales
frase_usuario = input("Ingresa una frase: ")
vocales_encontradas = contar_vocales(frase_usuario)
print(f"La frase contiene {vocales_encontradas} vocales.")
if __name__ == "__main__":
   contar_vocales(frase_usuario) 

# Ejercicio 5 Haz un programa que pida un número, y crea una nueva lista sin duplicados. Pide 10 números.
lista_numeros = []
for i in range(10):
    numero = input("Ingresa un número: ")
    lista_numeros.append(numero)
lista_sin_duplicados = list(set(lista_numeros))
print("Lista sin duplicados:", lista_sin_duplicados)