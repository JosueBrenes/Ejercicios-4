# = Solicitamos al usuario que digite el numero que quiere que se desplegue en la tabla 
print("Tabla de multiplicar")
tabla = int(input("Digite el numero que desea que se despliegue en la tabla: "))
for i in range(1,11):
    print(tabla, "x", i, "=", i*tabla) # = Imprimimos el resultado