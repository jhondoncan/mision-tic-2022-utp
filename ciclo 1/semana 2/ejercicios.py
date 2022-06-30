
# Condiciones simples

# Ejercicio que indica si un estudiante aprueba
""" nota = int(input("Ingrese la nota: "))
if nota >= 60:
    print("Aprobado")
if nota >= 90:
    print("Excelente")
if nota = 100:
    print("Yo creo que hiciste trampa")
 """

""" # Algoritmo que indica si un numero es positivo o negativo o cero
numero = int(input("Ingrese un numero: "))
if numero > 0:
    print(f'El numero {numero} es positivo')
if numero < 0:
    print(f'El numero {numero} es negativo')
if numero == 0:
    print(f'El numero es cero')
 """


""" # Algoritmo que indica que cantidad de digitos tiene un numero
numero = int(input("Ingrese un numero: "))
if numero < 10:
    print(f'El numero {numero} tiene un solo digito')
elif numero >= 10 and numero < 100:
    print(f'El numero {numero} tiene dos digitos')
elif numero >= 100 and numero < 1000:
    print(f'El numero {numero} tiene tres digitos')
elif numero >= 1000 and numero < 10000:
    print(f'El numero {numero} tiene cuatro digitos')
elif numero >= 10000 and numero < 100000:
    print(f'El numero {numero} tiene cinco digitos')
elif numero >= 100000 and numero < 1000000:
    print(f'El numero {numero} tiene seis digitos')
elif numero >= 1000000:
    print(f'El numero {numero} tiene siete o más digitos') """

""" # Algoritmo que convierte el peso de libras a kilos
def conversor(libras: float) -> str: #-> str significa lo que va a retornar en este caso un string
    return f'El peso en kilos es: {libras * 0.453592}'
libras = (float(input("Ingrese el peso en libras: ")))
print(conversor(libras)) """


""" # Menu de opciones con while
menu = input('**** MENU PRINCIPAL ****\n'
             '1 - Convertir millas a kilometros\n'
             '2 - Convertir kilometros a millas\n'
             '0 - Salir\n'
             'Ingrese una opcion: ')
while menu != '0':
    if menu == '1':
        millas = float(input('Ingrese la cantidad de millas: '))
        kilometros = millas * 1.60934
        print(f'La cantidad de millas {millas} son {kilometros} kilometros\n')
    elif menu == '2':
        kilometros = float(input('Ingrese la cantidad de kilometros: '))
        millas = kilometros / 1.60934
        print(f'La cantidad de kilometros {kilometros} son {millas} millas\n')
    else:
        print('Opcion incorrecta\n')
    menu = input('**** MENU PRINCIPAL ****\n'
                 '1 - Convertir millas a kilometros\n'
                 '2 - Convertir kilometros a millas\n'
                 '0 - Salir\n'
                 'Ingrese una opcion: ')
 """


""" #Poner palabras en mayusculas o minusculas
palabra = 'Doncan'
print(palabra)
print(f'Palabra en mayusculas {palabra.upper()}')
print(f'Palabra en minusculas {palabra.lower()}') """


""" # Borrar espacios en blanco al principio y final
frase = '  .  La programacion es lo mejor  .  '
print(f'Frase sin espacios: {frase.strip()}')
 """


""" #Preguntar si hay algo en el string
frase = 'Que tengas buen dia'
print(frase.startswith('Que'))
print(frase.endswith('dia')) """

""" # Buscar si hay algo en el string devuelve la posision
correo = 'arlem@misena.eud.co'
enlaposicion = correo.find('@')
print(enlaposicion) """


""" # Indica cuantas veces aparece una palabra en un string
frase = 'La programacion es lo mejor'
print(f"La frase tiene {frase.count('o')} 'o'")
print(frase.replace('o', '0'))  # Remplaza una palabra por otra
 """

""" coffee = 100

if coffee == 0:
    coffee.refill()
else:
    coffee.drink()
    coffe = coffee - 10
 """

""" # DICCIONARIOS
diccionario = {
    'documento': 1079607161,
    'nombres': 'Jhon Arlem',
    'apellidos': 'Silva Andrade',
    'profesion': 'Estudiante'
}
print(diccionario)
print(f"El nombre guardado en el diccionario es: {diccionario['nombres']}")
 """

# Promedio de notas con funciones y diccionarios
""" from math import *  # Cuando se importa asi no se utiliza . sino como funcion primitiva
from math import pi  # Solo importa pi i se utiliza sin .
import math  # Se utiliza la funcion por medio de un .
dicNotas = {}
dicNotas['nota1'] = 3.0
dicNotas['nota2'] = 2.1
dicNotas['nota3'] = 4.8
dicNotas['nota4'] = 4.7


def promedio(dicNotas):
    suma = 0
    for i in dicNotas:
        suma += dicNotas[i]
    return round(suma / len(dicNotas), 2)

    # return (dicNotas['nota1'] + dicNotas['nota2'] + dicNotas['nota3'] + dicNotas['nota4']) / 4


print(f' El promedio de la nota es: {promedio(dicNotas)}')
 """

# Manejo de exepciones Try - Except

""" try:
    a = int(input('Ingrese un numero entero: '))
    print(a)
except:
    print('Ha ocurrido un error en el sistema')
 """


##### IMPORTACION DE MODULOS #####
# Siempre que vamos a importar debe hacerce al inicio


# Algoritmo que calcula el area de un circulo


def areaCirculo(radio):
    area = math.pi * radio ** 2
    return round((f'El area del circulo es: {area}'), 2)


print(areaCirculo(int(input('Ingrese el radio del circulo: '))))

""" radio = float(input('Ingrese el radio del circulo: '))
area = math.pi * (radio ** 2)
print(f'El area del circulo es: {area}') """
