
def cliente(informacion: dict) -> dict:
    if informacion['edad'] > 18:
        atraccion = 'X-Treme'
        apto = True
        if informacion['primer_ingreso'] == True:
            ValorBoleta = 20000
            dscto = (ValorBoleta*0.05)
            total_boleta = ValorBoleta-dscto
        else:
            total_boleta = 20000
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if informacion['primer_ingreso'] == True:
            ValorBoleta = 5000
            dscto = (ValorBoleta*0.07)
            total_boleta = ValorBoleta-dscto
        else:
            total_boleta = 5000
    elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if informacion['primer_ingreso'] == True:
            ValorBoleta = 10000
            dscto = (ValorBoleta*0.05)
            total_boleta = ValorBoleta-dscto
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    resultado = {}
    resultado['nombre'] = informacion['nombre']
    resultado['edad'] = informacion['edad']
    resultado['atraccion'] = atraccion
    resultado['apto'] = apto
    resultado['primer_ingreso'] = informacion['primer_ingreso']
    resultado['total_boleta'] = total_boleta
    return resultado


informacionrmacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False
}
print(cliente(informacionrmacion))
