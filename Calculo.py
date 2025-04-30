from datetime import datetime

def calcular_anio_nacimiento(edad_actual):
    anio_actual = datetime.now().year
    anio_nacimiento = anio_actual - edad_actual
    return anio_nacimiento

def main():
    try:
        edad = int(input("Por favor, ingresa tu edad actual: "))
        anio_nacimiento = calcular_anio_nacimiento(edad)
        print(f"Tu año de nacimiento es aproximadamente: {anio_nacimiento}")
    except ValueError:
        print("Por favor, ingresa un número válido para la edad.")

if __name__ == "__main__":
    main()