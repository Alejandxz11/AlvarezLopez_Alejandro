










# Ejercicio 4: Pide 8 numeros, elimina las repeticiones y muestra la lista sin duplicados ordenados de menor a mayor
lista_numeros = [] 

for i in range(8):
    numero = input("Ingresa un número: ")
    lista_numeros.append(numero)

lista_numeros_ordenada = list(set(lista_numeros))
lista_numeros_ordenada.sort()
print(lista_numeros_ordenada)

# Ejercicio 5: Pide 10 calificaciones entre 0 y 10. Si alguna es menor a 6, añade al conteo de reprobados. Al final, muestra cuantos aprobaron y cuantos reprobaron. 
list_aprobados = []
list_reprobados = []

for i in range(10):
    calificacion = float(input("Ingresa una calificación entre 0 y 10: "))
    while calificacion < 0 or calificacion > 10:
        calificacion = float(input("Calificación inválida. Ingresa una calificación entre 0 y 10: "))
    if calificacion >= 6:
        list_aprobados.append(calificacion)
    else:
        list_aprobados.append(calificacion)

print("Número de aprobados:", len(list_aprobados))
print("Número de reprobados:", len(list_reprobados))

#Diccionarios
# nombre : "Mario"

diccionario = {
    "nombre": "Mario",
    "apellido": "Segovia",
    "edad": 29,
    "licenciatura": "Ingeniería en Sistemas Computacionales",
    "isEmpleado": True
}

print(diccionario.keys()) # Devuelve las claves del diccionario
print(diccionario.values()) # Devuelve los valores del diccionario 
print(diccionario.items()) # Devuelve agrupados en conjuntos la clave y el
print(diccionario["isEmpleado"]) #Accede a la clave deseada
diccionario.pop("edad") # Elimina una clave junto con su valor 
print(diccionario) 
print(len(diccionario)) #Devuelve el largo del diccionario

diccionario["edad"] = 29 # Agregar o actualizar un valor
print(diccionario)

# Recorrer un diccionario
for clave, valor in diccionario.items():
    print(f"La clave es: {clave}: {valor}")


# Ejercicio 1: Crea un diccionariovacío. Pide nombres y calificaciones de 5 alumnos y guardalos en el diccionario. Luego muestra su promedio.
diccionario_alumnos = {}
for i in range(5):
    nombre = input("Ingresa el nombre del alumno: ")
    calificacion = float(input("Ingresa la calificación de {nombre}: "))
    while calificacion < 0 or calificacion > 10:
        calificacion = float(input("Calificación inválida. Ingresa una calificación entre 0 y 10: "))
    diccionario_alumnos[nombre] = calificacion

print(diccionario_alumnos)

for clave, valor in diccionario_alumnos.items():
    print(f"La calificación de {clave} es: {valor}")

    suma_calificaciones = sum(diccionario_alumnos.values())
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio de las calificaciones es: {promedio}")


# Ejercicio 2: Crea un diccionario con 5 productos y sus precios. Pide un producto y muestra su precio. 
diccionario_productos = {
 "cloro": 20,
 "Detergente": 35,
 "jabón": 15,
 "Papel higiénico": 40,
 "limpiador multiusos": 60
}
producto_buscado = input("Ingresa el nombre del producto que deseas buscar: ")
if producto_buscado in diccionario_productos:
    print(f"El precio de {producto_buscado} es: ${diccionario_productos[producto_buscado]}")
else:
    print("El producto no se encuentra en el inventario.")

# Ejercicio 3: Crea un diccionario con 5 países y sus capitales. Pide un país y muestra su capital.
pais_buscado = input("Ingresa el nombre del país o 'salir' para terminar: ")
diccionario_paises = {
    "México": "Ciudad de México",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Argentina": "Buenos Aires",
    "Estados Unidos": "Washington D.C."
}
while pais_buscado != "salir":
    if pais_buscado in diccionario_paises:
    print(f"La capital de {pais_buscado} es: {diccionario_paises[pais_buscado]}")
else:
    capital_pais = input("El país no se encuentra en el diccionario. Ingresa la capital de ese país para agregarlo: ")
    
    diccionario_paises[pais_buscado] = capital_pais
    pais_buscado = input("Ingresa el nombre del país o 'salir' para terminar: ")