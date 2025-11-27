#1 Pide al usuario la temperatura de 7 días y muestra el promedio semanal

temperaturas = []
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    temperaturas.append(temp)

promedio = sum(temperaturas) / len(temperaturas)
print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

#2 Haz un programa que solicite una oración y reemplaza todas las letras a, i, u por el carácter #

oracion = input("Escribe una oración: ")
nueva_oracion = ""
for letra in oracion:
    if letra.lower() in "aiu":
        nueva_oracion += "#"
    else:
        nueva_oracion += letra
print("Oración modificada:", nueva_oracion)

#3 Pide un número entero y calcula cuantos números impares existen entre 1 y N 

N = int(input("Introduce un número entero: "))
cantidad_impares = (N + 1) // 2
print(f"Cantidad de números impares entre 1 y {N}: {cantidad_impares}")

#4 Solicita el nombre de 5 animales. Guárdalos en un arreglo y muestra solo aquellos cuyos nombres comiencen con una vocal

animales = []
for i in range(5):
    nombre = input(f"Ingresa el nombre del animal {i+1}: ")
    animales.append(nombre)

vocales = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
print("Animales cuyos nombres comienzan con una vocal:")
for animal in animales:
    if animal.startswith(vocales):
        print(animal)  

#5 Pide al usuario ingresar 5 precios (Se aceptan con punto decimal), guárdalos en una lista y calcula el total. Si el total supera $500, muestra "Compra alta"; si es menor de $500 muestra "Compra baja" si todos los precios son mayores a $100, muestra además "Productos premium"

precios = []
for i in range(5):
    precio = float(input(f"Ingrese el precio {i+1}: "))
    precios.append(precio)

total = sum(precios)

if total > 500:
    print("Compra alta")
else:
    print("Compra baja")

if all(precio > 100 for precio in precios):
    print("Productos premium")

#6 Solicita 6 titulos de canciones y muéstranos en orden alfabetico inverso (Es decir, de Z a A)

canciones = []
for i in range(6):
    titulo = input(f"Ingresa el título de la canción {i+1}: ")
    canciones.append(titulo)

canciones.sort(reverse=True)

print("Canciones en orden alfabético inverso:")
for cancion in canciones:
    print(cancion)

#7 Pide un número entero y determina si es divisibe entre 4, entre 6 o entre ambos

numero = int(input("Introduce un número entero: "))
if numero % 4 == 0 and numero % 6 == 0:
    print(f"El número {numero} es divisible entre 4 y 6.")
elif numero % 4 == 0:
    print(f"El número {numero} es divisible entre 4.")
elif numero % 6 == 0:
    print(f"El número {numero} es divisible entre 6.")
else:
    print(f"El número {numero} no es divisible ni entre 4 ni entre 6.")

#8 Solicita el nombre de un personaje ficticio, su especie y su planeta. Luego imprime el mensaje: "Es un(a){especie} que proviene del planeta {planeta}

nombre = input("Ingresa el nombre de un personaje ficticio: ")
especie = input("Ingresa la especie del personaje: ")
planeta = input("Ingresa el planeta de origen del personaje: ")
print(f"Es un(a) {especie} que proviene del planeta {planeta}.")