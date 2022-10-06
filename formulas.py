import datetime

# 1 - suma, resta, producto y división de 2 numeros con impresion de pantalla.
def funciones_primarias():
    try: 
        num1 = int(input('Ingrese el primer numero: '))
        num2 = int(input('Ingrese el segundo numero: '))
        division = 'No se puede dividir por cero' if num2 == 0 else f'la division es {num1/num2}'
        return print(f'La suma es: {num1 + num2} \nLa resta es: {num1 - num2} \nLa multiplicacion es: {num1 * num2} \n{division}') 
    except ValueError: 
        return print('Los numeros ingresados deben ser enteros.')

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

# 3 - Cantidad a cobrar del cliente. Validar ingreso del mes de acuerdo a un ingreso, descuento octubre 15%.
def importe_total_en_compra():
    try:
        mes = int(input('Ingrese el numero de mes de la compra: ')) 
        while 1> mes or mes >12:
            mes = int(input('El mes debe ser un numero entero del 1 al 12: ')) 
        importe = float(input('Ingrese el importe de la compra: '))
        mes_descripcion = datetime.date(1900, mes, 1).strftime('%B')
        porcentaje = 0.15 if mes == 10 else 0.0
        importe_total = importe*(1-porcentaje) 
        mns = f'Importe Original: {importe} $ \nDescuento: {importe*-porcentaje} $ \nImporte Total: {importe_total} $'
        return f'Detalle de las compras del mes de {mes_descripcion}: \n{mns}'
    except ValueError: 
        return 'Se debe ingresar un numero entero.'

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
def saludo():
    for i in range(1,6):
        print("Hola")

# 6 - escribir un numero y obtener los numeros pares menor a este.
def suma_pares(numero):
    numeros_pares = [x for x in range(0,numero+1) if x % 2 == 0]
    return f'La suma de todos los numeros pares anteriores a {numero} es: {sum(numeros_pares)}'

# 7 - Pedir un numero y devolver el mes. Validar ingreso.
def imprime_mes ():
    meses_validos=('enero', 'febrero', 'marzo', 'abril','mayo', 'junio', 'julio', 'agosto', 'septiembre','octubre', 'noviembre','diciembre')

    mes=int(input('Ingrese un número de mes (del 1 al 12): '))
    if mes in range(1,13):
        print(f'El mes seleccionado es {meses_validos[mes-1]}')
    else: 
        print('Debe ingresar números de 1 a 12')

# 8 - Suma y promedio de 10 valores.
def valores():
   acum=0
   prom=0
   cont=0
   for i in range(0,10):
        numero = int(input("ingrese numero: "))
        acum+=numero
        cont+=1
        prom=acum/cont
   return prom,acum
# 9 - Imprimir la suma de los números impares del 1 al 25.
def suma_impares_hasta_25():
    numeros = [x for x in range(0,26) if x % 2 != 0]
    return sum(numeros)
