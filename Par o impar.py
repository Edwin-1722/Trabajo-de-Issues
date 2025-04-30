def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

# Solicitar al usuario un número
try:
    numero = int(input("Introduce un número: "))
    print(es_par_o_impar(numero))
except ValueError:
    print("Por favor, introduce un número válido.")