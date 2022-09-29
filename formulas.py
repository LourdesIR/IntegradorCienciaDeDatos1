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

# 3 - Cantidad a cobrar del cliente.  Validar ingreso del mes de acuerdo a un ingreso. 
# Discriminar en las impresiones de pantalla los valores referidos al total, descuento e importe a pagar final. 

# 4 - Codigo de calificaciones docentes. validacion de notas.
def calificando_alumnos():
    _desaprobado = 'Ha desaprobado.'
    _aprobado = 'Ha obtenido un aprobado.'
    _calificacion_mayor = 'Ha obtenido una calificacion '

    tabla_calificaciones ={
                    1: _desaprobado,
                    2: _desaprobado,
                    3: _desaprobado,
                    4: _aprobado,
                    5: _aprobado,
                    6: _aprobado,
                    7: f'{_calificacion_mayor}notable.',
                    8: f'{_calificacion_mayor}notable.',
                    9: f'{_calificacion_mayor}sobresaliente.',
                    10: f'{_calificacion_mayor}sobresaliente.',
                    }
    try: 
        calificacion = int(input('Ingrese la calificacion del alumno: '))
    except ValueError: 
        return 'Se debe ingresar un numero entero.'
        
    if calificacion in tabla_calificaciones.keys():
        return f'La calificación es {calificacion} {tabla_calificaciones[calificacion]}'
    else: 
        return 'Calificacion invalida.'

# 5 - Programa que escriba hola 5 veces.

# 6 - escribir un numero y obtener los numeros pares menor a este.

# 7 - Pedir un numero y devolver el mes. Validar ingreso.

# 8 - Suma y promedio de 10 valores.

# 9 - Imprimir la suma de los números impares del 1 al 25.
def suma_impares_hasta_25():
    numeros = [x for x in range(0,26) if x % 2 != 0]
    return sum(numeros)
