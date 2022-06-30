import pandas as pd
print("\x1Bc")

serie = pd.Series(['Habilidades', 'Ingles', 'Programacion'])
print(serie)

print("Series atravez de diccionario")
serieD = pd.Series({'Habilidades': 4.5, 'Ingles': 4.5, 'Programacion': 5})
print(serieD)
print("Series a travez de tuplas")
serieT = pd.Series({(1, 2, 3, 4, 5)})
print(serieT)


# Indice impliicito y explicito
print("\nIndice implicito y explicito")
