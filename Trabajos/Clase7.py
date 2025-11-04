# Ejercicio 3: Haz un programa en Python que pida un numero entero y muestre cuantos numeros pares hay desde 1 hasta ese número entero y muestre cuantos números pares hay desde 1 hasta ese número (incluyéndolo si es par)

conteo_pares = 0
#Solicitar al usuario que ingrese un numero entero 
numero = int(input("Ingrese un numero entero: "))

for i in range (1, numero +1): numero = 6
if i % 2 == 0:
   conteo_pares +=1
print(i)

print(f"Hay {conteo_pares}) numeros pares desde 1 hasta {numero}.")

#Ejercicio 4 haz un programa en Python que pida un número y calcule el factorial de ese número utilizando un ciclo for

numero = int (input("Ingrese un número para calcular su factorial: "))
factorial= 1
for i in range(1, numero + 1 ):
    factorial *= i
print(f"El factorial de {numero} es {factorial}.")

# Bucle While
















