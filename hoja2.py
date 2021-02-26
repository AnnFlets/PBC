print("===== Iniciar sesión como invitado =====")
print()
print("Ingrese una contraseña: " )
contraseña = input()
print()
print("¡Contraseña ingresada con éxito!")
a = 5
while a >= 4:
    print()
    print("Ingrese la contraseña para iniciar sesión: ")
    contraseña2 = input()
    if contraseña2.lower() == contraseña.lower():
        print()
        print("===== Contraseña correcta =====")
        break
    else:
        print()
        print("===== Ingreso una contraseña incorrecta. Intente nuevamente =====")
        continue
print()
print("Fin del Programa 1.")
print()
print()
print("===== Encontrar grupo al que pertenecen los alumnos =====")
print()
print("Ingrese el nombre del alumno: ")
nombre = input()
print()
inicial = nombre[0]
print("Ingrese el sexo del alumno (M para hombre y F para mujer): ")
sexo = input()
print()
if sexo.lower() == "f":
    if inicial.lower() < "m":
        print("===== El alumno pertenece al grupo A =====")
    else:
        print("===== El alumno pertenece al grupo B =====")
elif sexo.lower() == "m":
    if inicial.lower() > "n":
        print("===== El alumno pertenece al grupo A =====")
    else:
        print("===== El alumno pertenece al grupo B =====")
print()
print("Fin del Programa 2")