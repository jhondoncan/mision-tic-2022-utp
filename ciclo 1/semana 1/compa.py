def CDT(Usuario: str, Capital: int, Tiempo: int):
    if Tiempo <= 2:
        ValorAperder = Capital * 0.02
        ValorTotal = Capital + ValorAperder
        return (f'Para el usuario {Usuario} La cantidad de dinero a recibir, según el monto inicial {Capital} para un tiempo de {Tiempo} meses es: {ValorTotal}')
    else:
        ValorInteres = (Capital * 0.03 * Tiempo)/12
        ValorTotal = Capital + ValorInteres
        return (f'Para el usuario {Usuario} La cantidad de dinero a recibir, según el monto inicial {Capital} para un tiempo de {Tiempo} meses es: {ValorTotal}')


print(CDT('AB1012', 1000000, 3))
print(CDT('ER3366', 650000, 2))
