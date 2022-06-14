""" print('-Hola, como estas?')
print('-Hello, how are you?')
print('-Oi, como vai?')
 """

""" print("'Buenas tardes' \n'Good afternoon'\n'boa tarde'") """

""" print('    ____')
print('   /  () \ ')
print(' _|_______|_')
print('| | ====  | |')
print('|_|   o   |_|')
print(' ||   o   ||')
print(' ||___ ___||')
print('|~ \_____/~ |')
print('/=\ /=\ /=\\')
print('[ ] [ ] [ ]') """

""" f = int(input("Ingrese los grados Fharenheit: "))
c = (f-32)*5/9
print(f, "grados Fharenheit equivalen a:", c, "Celsius.") """

""" c = int(input("Ingrese los grados Centigrados: "))
f = (c*9/5)+32
print(c, "grados Celsius equivalen a:", f, "Fharenheit.") """


""" ##### Programa que calcula el indice de masa corporal #####

peso = float(input("Ingrese su peso en kg:"))
altura = float(input("Ingrese su altura en centimetros:"))
imc = peso / ((altura/100)**2)
print("Su indice de masa corporal es:", imc)

 """
""" ## Programa de censo ##
nombre = input("Ingrese su nombre: ")
nacimiento = input("Ingrese su fecha de nacimiento: ")
edad = int(input("Ingrese su edad: "))
ocupacion = input("Ingrese su ocupacion: ")
casa = input("Ingrese su numero de casa: ")
nombreCalle = input("Ingrese el nombre de la calle: ")
pueblo = input("Ingrese el nombre del pueblo: ")
personas = int(input("Ingrese el numero de personas que viven en su casa: "))
civil = input("Ingrese su estado civil: ")

print("Censo guardado para el usuario:", nombre, "Informacion almacenada: Fecha de nacimiento: ", nacimiento,
      "Edad: ", edad, "Ocupacion: ", ocupacion, "Numero de casa: ", casa, "Nombre de la calle", nombreCalle, "Pueblo: ", pueblo, "Numero de personas que viven en su casa: ", personas, "Estado civil: ", civil)
 """

""" ## Programa calculadora ##
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
divicion = n1 / n2
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la multiplicacion es:", multiplicacion)
print("El resultado de la division es:", divicion)
 """

""" # Programa que dice si dos numeros son iguales o diferentes
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
if n1 == n2:
    print("Los numeros son iguales")
else:
        print("Los numeros son diferentes")


# Porgrama que lee cuatro numeros y dice cual es el mayor
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
n4 = int(input("Ingrese el cuarto numero: "))
resultado = max(n1, n2, n3, n4)
print("El numero mayor es:", resultado) """

""" # Programa para saber si un numero es par o impar
n = int(input("Ingrese un numero: "))
if n % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
 """

""" # Programa para saber si un numero es primo o no
numero = int(input("Ingrese un numero: "))
if numero == 1:
    print("El numero es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")

 """


""" def sumar(a: int, b: int):
     return a + b 
    return (f'La suma es: {a + b}')


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
print(sumar(a, b)) """

""" 
# Funcion que retorna la suma de dos numeros float
def sumar(num1: float, num2: float):
    return print((f'La suma de {num1} y {num2} es: {num1 + num2}'))


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
sumar(num1, num2) """


# Funcion que retorna la raiz cuadrada de un numero float
def raiz(num: float):
    return print((f'La raiz cuadrada de {num} es: {num**0.5}'))


num = float(input("Ingrese un numero para calcular la raiz cuadrada: "))
raiz(num)
