class Empleado:
    def __init__(empleado):
        empleado.nombre = input("Ingrese nombre: ")
        empleado.salario = int(input("Ingrese salario: "))

    def imprimir(empleado):
        print('****************************************')
        print("Nombre: ", empleado.nombre)
        print("Salario: ", empleado.salario)

    def pagarImpuestos(empleado):
        if empleado.salario > 3000:
            print(f'El usuario {empleado.nombre} debe pagar impuestos')
            print('****************************************')
        else:
            print(f'El usuario {empleado.nombre} no debe pagar impuestos')
            print('****************************************')
