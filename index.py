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

# feature/funcion-dividir:

def dividir(a, b):
    return a / b

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
                    break # Cierra el ciclo de las operaciones.
                elif seleccionDeOperacion == 2:
                    establecerValores()
                    print(f"\nResultado de Restar {primerValor} con {segundoValor}: {restar(primerValor, segundoValor)}")
                    break # Cierra el ciclo de las operaciones.
                elif seleccionDeOperacion == 3:
                    establecerValores()
                    print(f"\nResultado de Multiplicar {primerValor} con {segundoValor}: {multiplicar(primerValor, segundoValor)}")
                    break # Cierra el ciclo de las operaciones.
                elif seleccionDeOperacion == 4:
                    establecerValores()
                    print(f"\nResultado de dividir {primerValor} con {segundoValor}: {dividir(primerValor, segundoValor)}")
                    break # Cierra el ciclo de las operaciones.
                else:
                    print("\n\n¡¡ADVERTENCIA!!\n<<Debe colocar un valor numérico entero entre 1 y 4, de lo contrario no empezara la operación.>>\n\n")
            except ValueError:
                print("\n\n¡¡ADVERTENCIA!!\n<<Probablemente esta intentado ingresa valores no numéricos como caracteres o símbolos.\nDebe colocar un valor numérico entero, de lo contrario no se realizara la operación.>>\n\n")
        while True:
            try:
                
                print("\n\n¿Desea repetir o salir de la calculadora?\n\nPara Salir Coloque 0.\nPara repetir coloque 1.\n")
                
                seleccionRepetir = int(input("Coloque aquí su selección: "))
                
                if seleccionRepetir == 0:
                    print("\n\nHasta luego!")
                    break # Cierra el ciclo de selección de repetición o salida.
                elif seleccionRepetir == 1:
                    print("\n\nContinuamos pues..\n\n")
                    break # Cierra el ciclo de selección de repetición o salida.
                else:
                    print("\n\n¡¡ADVERTENCIA!!\n<<Debe colocar un valor numérico entero que sea 0 o 1, de lo contrario no se sabra si quiere salir o repetir.>>\n\n")
            except ValueError:
                print("\n\n¡¡ADVERTENCIA!!\n<<Probablemente esta intentado ingresa valores no numéricos como caracteres o símbolos.\nDebe colocar un valor numérico entero, de lo contrario no se realizara la operación.>>\n\n")
        
        if seleccionRepetir == 0:
            break # Cierra el ciclo del programa.
    except ValueError:
        print("\n\n¡¡ADVERTENCIA!!\n<<Debe colocar un valor numérico entero (1, 2, 3 o 4), de lo contrario no se realizara la operación.>>\n\n")