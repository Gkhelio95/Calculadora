def calculadora():
    print("Bienvenido a la calculadora")
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        try:
            operacion = int(input("\nIngrese el número de la operación que desea realizar (1-4): "))
            if operacion in [1, 2, 3, 4]:
                break
            else:
                print("Error: Por favor ingrese un número entre 1 y 4.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == 1:
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif operacion == 2:
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif operacion == 3:
            resultado = num1 * num2
            print(f"\nResultado: {num1} × {num2} = {resultado}")
        elif operacion == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} ÷ {num2} = {resultado:.2f}")
            else:
                print("\nError: No se puede dividir entre cero.")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")

if __name__ == "__main__":
    calculadora()