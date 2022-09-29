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

# 5 - Programa que escriba hola 5 veces.
def saludo():
    for i in range(1,6):
        print("Hola")

# 6 - escribir un numero y obtener los numeros pares menor a este.

# 7 - Pedir un numero y devolver el mes. Validar ingreso.

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
