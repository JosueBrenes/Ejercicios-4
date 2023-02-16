# = Declaracion de variables
notaMayor = 0
notaMenor = 100
nota = 0
cantidadAprobados = 0
cantidadReprobados = 0

# = Ejecucion del ciclo de manera "Infinita"
# = Hasta que el ususario decida
while nota >= 0 and nota <= 100:
    #Solicita la nota del estudiante
    nota = int(input("Digite la nota del estudiante: "))

    # = Evalua la nota
    if nota >= 0 and nota <= 100:
        #Aprovados y reprobados 
        if nota >= 70:
            cantidadAprobados += 1
        else: 
            cantidadReprobados += 1

        # = Nota mayor y menor
        if nota > notaMayor:
            notaMayor = nota

        if nota < notaMenor:
            notaMenor = nota

# = Imprimimos el resultado
print(cantidadAprobados, "han aprobado el curso")
print(cantidadReprobados, "han reprobado el curso")
print(notaMayor, "es la nota mas alta del curso")
print(notaMenor, "es la nota mas baja del curso")