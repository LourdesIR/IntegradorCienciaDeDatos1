# 1 - suma, resta, producto y división de 2 numeros con impresion de pantalla.

def suma(a, b):
    return print(f'La suma de ambos valores: {int(a + b)}')    
def resta(a, b):
    return print(f'La resta de ambos valores: {int(a - b)}')  
def multiplicacion(a, b):
    return print(f'La multiplicación de ambos valores: {int(a * b)}') 
def division(a, b):
    if (b != 0):
        return print(f'La división de ambos valores: {a / b}')
    else:
        return print("No se puede dividir por cero")
print('_____________________ Inicio del programa ejercicio 1 _____________________-')
print("Ingrese 2 numeros enteros")
a = float(input('Primer valor: '))
while(a%1 != 0):
    a = float(input('El valor debe ser ENTERO sin comas, Ingrese otro valor: '))

b = float(input('Segundo valor: '))
while(b % 1 != 0):
    b = float(input('El valor debe ser ENTERO sin comas, Ingrese otro valor: '))

print(f'los valores ingresados fueron: {int(a)} y {int(b)}')
suma(a,b)
resta(a,b)
multiplicacion(a,b)
division(a,b)

# 2 - el mayor de 3 numeros enteros ingresados por el usuario. mostrar resultado y los 3 numeros por pantalla.
def numero_max(numeros=[]):
    _numeros = numeros
    _puestos={0:'primer',1:'segundo',2:'tercer'}

    while len(_numeros) < 3:
        numero = int(input(f'Ingrese el {_puestos[len(_numeros)]} numero: '))
        if numero in _numeros:
            print('Ese número ya esta registrado.')
            continue
        _numeros.append(numero)
    print(f'Numeros ingresados: {_numeros[0]}, {_numeros[1]}, {_numeros[2]}.')

    resultado = f'De los numeros ingresados, {max(_numeros)} es el mayor.'
    return resultado

# 3 - Cantidad a cobrar del cliente.  Validar ingreso del mes de acuerdo a un ingreso. 
# Discriminar en las impresiones de pantalla los valores referidos al total, descuento e importe a pagar final. 

# 4 - Codigo de calificaciones docentes. validacion de notas.

# 5 - Programa que escriba hola 5 veces.

# 6 - escribir un numero y obtener los numeros pares menor a este.
def suma_pares(numero):
    numeros_pares = [x for x in range(0,numero+1) if x % 2 == 0]
    return f'La suma de todos los numeros pares anteriores a {numero} es: {sum(numeros_pares)}'

# 7 - Pedir un numero y devolver el mes. Validar ingreso.

# 8 - Suma y promedio de 10 valores.

# 9 - Imprimir la suma de los números impares del 1 al 25.
