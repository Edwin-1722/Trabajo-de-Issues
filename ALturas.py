def encontrar_alturas():
    alturas = []

    print("Ingrese las alturas en centímetros (escriba 'fin' para terminar):")
    while True:
        entrada = input("Altura: ")
        if entrada.lower() == 'fin':
            break
        try:
            altura = float(entrada)
            alturas.append(altura)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if alturas:
        altura_max = max(alturas)
        altura_min = min(alturas)
        print(f"La altura mayor es: {altura_max} cm")
        print(f"La altura menor es: {altura_min} cm")
    else:
        print("No se ingresaron alturas.")

# Llamar a la función
encontrar_alturas()