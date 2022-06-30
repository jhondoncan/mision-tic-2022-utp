def cliente(informacion: dict) -> dict:
    if informacion['edad'] > 18:
        atraccion: str = 'X-Treme'
        valorBoleta: int = 20000
        if informacion['primer_ingreso'] == True:
            descuento: float = 0.05
        else:
            descuento: float = 0
        totalBoleta: float = valorBoleta - (valorBoleta * descuento)
        ticket = {
            'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': atraccion,
            'apto': True,
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': totalBoleta
        }
        return ticket
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion: str = 'Carros chocones'
        valorBoleta: int = 5000
        if informacion['primer_ingreso'] == True:
            descuento: float = 0.07
        else:
            descuento: float = 0
        totalBoleta: float = valorBoleta - (valorBoleta * descuento)
        ticket = {
            'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': atraccion,
            'apto': True,
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': totalBoleta
        }
        return ticket
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        atraccion: str = 'Sillas voladoras'
        valorBoleta: int = 10000
        if informacion['primer_ingreso'] == True:
            descuento: float = 0.05
        else:
            descuento: float = 0
        totalBoleta: float = valorBoleta - (valorBoleta * descuento)
        ticket = {
            'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': atraccion,
            'apto': True,
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': totalBoleta
        }
        return ticket
    elif informacion['edad'] <= 6:
        atraccion: str = 'N/A'
        totalBoleta: str = 'N/A'
        ticket = {
            'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': atraccion,
            'apto': False,
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': totalBoleta
        }
        return ticket


informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False
}
print(cliente(informacion))
