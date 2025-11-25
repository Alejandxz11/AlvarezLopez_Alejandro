#Realiza las siguientes 3 funciones 

#Función para buscar estudiante por medio del apellido
def buscar_estudiante_por_apellido(lista, apellido):
	for estudiante in lista:
		if estudiante["apellido"].lower() == apellido.lower():
			print("Estudiante encontrado:", estudiante)
			return
	print("No se encontró ningún estudiante con ese apellido.")

#Funcion para calcular el promedio del grupo

def calcular_promedio(grupo):
	suma = 0
	for nota in grupo:
		suma += nota
	promedio = suma / len(grupo)
	return promedio

#Funcion para ordenar estudiantes por promedio (de la calificación más alta a la más baja)

def ordenar_por_promedio(estudiantes):
	estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['promedio'], reverse=True)
	return estudiantes_ordenados
