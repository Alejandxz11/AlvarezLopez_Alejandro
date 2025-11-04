1# Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo.

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