print("Edad de un estudiante: ".center(50,"*"))
edad=int(input("Ingrese su edad: "))

def edad_actual(edad_estudiante):
    if edad_estudiante <18:
        print("El estudiante es menor de edad ")
    else:
        print("El estudiante es mayor de edad")
edad_actual(edad)