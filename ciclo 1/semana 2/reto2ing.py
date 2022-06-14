
informacion = {'id_cliente': 1,
               'nombre': 'Johana Fernandez',
               'edad': 20,
               'primer_ingreso': True}


dic_2 = {}


def cliente(informacion: dict) -> dict:
    if informacion['edad'] > 18:
        dic_2['atraccion'] = 'X-Treme'
        dic_2['apto'] = True

        if informacion['primer_ingreso'] == True:
            dic_2['total_boleta'] = (20000-(20000*0.05))
        else:
            dic_2['total_boleta'] = 20000
    return dic_2
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        dic_2['atraccion'] = 'Carros chocones'
        dic_2['apto'] = True
        if informacion['primer_ingreso'] == True:
            dic_2['total_boleta'] = (5000-(5000*0.07))
        else:
            dic_2['total_boleta'] = 5000
    elif informacion['edad'] >= 7 and informacion['edad'] <= 15:
        dic_2['atraccion'] = 'Sillas voladoras'
        dic_2['apto'] = True
        if informacion['primer_ingreso'] == True:
            dic_2['total_boleta'] = (10000-(10000*0.05))
        else:
            dic_2['total_boleta'] = 10000
    else:
        dic_2['atraccion'] = 'N/A'
        dic_2['apto'] = False
        dic_2['total_boleta'] = 'N/A'
    return (dic_2)


print(dic_2)
