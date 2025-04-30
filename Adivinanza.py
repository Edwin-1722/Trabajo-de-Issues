print("Adivinanza de un numero: ")
numero= int(input("Ingrese un numero. "))

def numero_adivinanza(adi_numero):
    if adi_numero ==7:
        print("El número es correcto.")
    else:
        print("El número es incorrecto.")
numero_adivinanza(numero)