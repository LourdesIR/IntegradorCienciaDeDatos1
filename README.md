# Uso
Recomiendo utilizar el programa desde la terminal, importando sus funciones directamente.
Para ello, primero debemos movernos al directorio donde tenemos nuestro archivo y entonces ejecutar el siguiente comando:
```bash
python or python3
```
y luego importamos todas las funciones con:
```python
from formulas import *
```
Ahora ya tenemos todas las funciones importadas, sientase libre de explorar las mismas.
## Funcionamiento
Cada función debe ser invocada como se indica en el titulo respectivo.
### 1 - operaciones(a,b)
Se usa invocandola y pasandole 2 paremetros de tipo entero, la misma devuelve la suma, resta, el producto y el cociente entre ambos numeros.
```python
```
### 2 - numero_max()
Pide 3 números enteros por teclado, comprueba que sean distintos y devuelve una cadena de texto explicando cual es el mayor. Tambien se le puede pasar la lista de numeros por parametro.
```python
>>> numero_max()
Ingrese el primer numero: 1
Ingrese el segundo numero: 2
Ingrese el tercer numero: 3
Numeros ingresados: 1, 2, 3.
'De los numeros ingresados, 3 es el mayor.'

o

>>> numero_max(numeros=[1,2,3])
Numeros ingresados: 1, 2, 3.
'De los numeros ingresados, 3 es el mayor.'
```
### 3 - simula_descuento()
Una tienda ofrece un descuento del 15% sobre el total de la compra basado en el mes en transcurso. Dado un mes y un importe, calcula si corresponde aplicar un descuento y devuelve un ticket con toda la información solicitada.
```python
```
### 4 - calificando_alumnos()
Recibe una calificación y devuelve una cadena con información.
```python
>>> calificando_alumnos()
Ingrese la calificacion del alumno: 10
'La calificación es 10 Ha obtenido una calificacion sobresaliente.'
```
### 5 - saludo()
Imprime hola 5 veces.
```python
>>> saludo()
Hola
Hola
Hola
Hola
Hola
```
### 6 - suma_pares(numero)
Se debe invocar la funcion y pasarle un numero por parametro, se generará una lista con todos los números pares menores al número enviado, y se devuelve la suma de los mismos.
```python
>>> print(suma_pares(150))
La suma de todos los numeros pares anteriores a 150 es: 5700
```
### 7 - imprime_mes()
Recibe un mes en formato numerico y devuelve el nombre del mismo.
```python
```
### 8 - valores()
Recibe 10 valores ingresados por teclado y devuelve el prmedio y la suma de los mismos.
```python
>>> valores()
ingrese numero: 1
ingrese numero: 2
ingrese numero: 3
ingrese numero: 4
ingrese numero: 5
ingrese numero: 6
ingrese numero: 7
ingrese numero: 8
ingrese numero: 9
ingrese numero: 10
(5.5, 55)
```
### 9 - suma_impares_hasta_25()
Devuelve la suma de todos los numeros impares debajo del 25.
```python
>>> suma_impares_hasta_25()
169
```