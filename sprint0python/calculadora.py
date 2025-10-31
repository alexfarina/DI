from operaciones import suma, resta, multiplicacion, division

opciones = ['suma', 'resta', 'multiplicacion', 'division']

nuevaOpe = ''

def seleccionar_opcion():
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    operacion = input('Selecciona una operación (suma, resta, multiplicacion, division): ')

    while operacion not in opciones:
        print("Escoge una operación válida")
        operacion = input('Selecciona una operación (suma, resta, multiplicacion, division): ')

    if operacion == 'suma':
        print(suma(num1, num2))
    elif operacion == 'resta':
        print(resta(num1, num2))
    elif operacion == 'multiplicacion':
        print(multiplicacion(num1, num2))
    elif operacion == 'division':
        print(division(num1, num2))

while nuevaOpe != 'n':
    seleccionar_opcion()
    nuevaOpe = input("Quieres realizar otra operacion (s para nueva operacion, n para salir)? ").lower()
