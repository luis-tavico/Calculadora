def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")

    opcion = input("Selecciona una opción (1-2): ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {restar(num1, num2)}")
    else:
        print("Opción inválida")
