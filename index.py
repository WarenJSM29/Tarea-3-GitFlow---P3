print("¡Hola Mundo!")

# variables:
primerValor, segundoValor = (0, 0)

def establecerValores():
    global primerValor, segundoValor
    
    primerValor = int(input("\nColoque un el primer valor: "))
    segundoValor = int(input("\nColoque un el segundo valor: "))
    return primerValor, segundoValor

# feature/funcion-para-sumar:

def sumar(a, b):
    return a + b

# feature/funcion-restar:

def restar(a, b):
    return a - b

# feature/funcion-multiplicar:

def multiplicar(a, b):
    return a * b

print("Bienvenido a la calculadora mas básica del mundo.\n\n")

while True:
    try:
        print("-- Menu de la Calculadora --\n\nSelecciona la operación que quieres realizar colocando su numero de orden:\n\n1. Suma\n2. Resta\n3. Multiplicación\n4. Division\n")
        
        seleccionDeOperacion = int(input("Coloca tu selección aquí: "))
        while True:
            try:
                if seleccionDeOperacion == 1:
                    establecerValores()
                    print(f"\nResultado de Sumar {primerValor} y {segundoValor}: {sumar(primerValor, segundoValor)}")
                    break
                elif seleccionDeOperacion == 2:
                    establecerValores()
                    print(f"\nResultado de Restar {primerValor} con {segundoValor}: {restar(primerValor, segundoValor)}")
                    break
                elif seleccionDeOperacion == 3:
                    establecerValores()
                    print(f"\nResultado de Multiplicar {primerValor} con {segundoValor}: {multiplicar(primerValor, segundoValor)}")
                    break
            except ValueError:
                print("\n\n¡¡ADVERTENCIA!!\n<<Debe colocar un valor numérico entero, de lo contrario no se realizara la operación.>>\n\n")
        break
    except ValueError:
        print("\n\n¡¡ADVERTENCIA!!\n<<Debe colocar un valor numérico entero (1, 2, 3 o 4), de lo contrario no se realizara la operación.>>\n\n")