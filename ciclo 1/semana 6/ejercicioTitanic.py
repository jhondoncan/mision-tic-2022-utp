import matplotlib.pyplot as plt
import pandas as pd

print("\x1Bc")

# Leyendo archivo csv graficar personas que sobrevivieron y murieron en el Titanic

# 1 Leer archivo csv
df = pd.read_csv('titanic.csv')
print(df)
cantdidad = df.survived.value_counts()
print(cantdidad)
print('Fallecidos: ', cantdidad[0])
print('Sobrevivientes: ', cantdidad[1])
# Grafica
x = ['Sobrevivientes']
y = [cantdidad[1]]
x2 = ['Fallecidos']
y2 = [cantdidad[0]]
plt.bar(x, y, color='blue', label='Sobrevivientes')
plt.bar(x2, y2, color='red',  label='Fallecidos')
plt.title('Sobrevivientes y fallecidos en el Titanic')
plt.xlabel('Personas')
plt.ylabel('Cantidad')
plt.legend()
plt.grid()
plt.show()
