import matplotlib.pyplot as plt

print("\x1Bc")
# Ejes x, y
""" x = ['Reto 1', 'Reto 2', 'Reto 3', 'Reto 4', 'Reto 5']  # Retos
y = [1, 2, 1.5, 1.9, 1.8]  # Tiempo horas

plt.plot(x, y, color='blue', linewidth=3, label='Tiempo de retos')
plt.title('Tiempo de resolucion de retos Misión TIC 2022')
plt.xlabel('Retos')
plt.ylabel('Tiempo (horas)')
plt.legend()
plt.grid() """
plt.show()

# Graficar doble linea
""" x30 = ['Reto 1', 'Reto 2', 'Reto 3', 'Reto 4', 'Reto 5']  # Retos
y30 = [1, 2, 1.5, 1.9, 1.8]  # Tiempo horas
x14 = ['Reto 1', 'Reto 2', 'Reto 3', 'Reto 4', 'Reto 5']  # Retos
y14 = [1.5, 2.2, 2, 1.7, 2.3]  # Tiempo horas

plt.plot(x30, y30, color='blue', linewidth=3, label='Grupo 30')
plt.plot(x14, y14, color='red', linewidth=3, label='Grupo 14')
plt.title('Tiempo de resolucion de retos Misión TIC 2022')
plt.xlabel('Retos')
plt.ylabel('Tiempo (horas)')
plt.legend()
plt.grid()
plt.show() """

# Graficar con barras
x30 = ['Reto 1', 'Reto 2', 'Reto 3', 'Reto 4', 'Reto 5']  # Retos
y30 = [1, 2, 1.5, 1.9, 1.8]  # Tiempo horas
x14 = ['Reto 1', 'Reto 2', 'Reto 3', 'Reto 4', 'Reto 5']  # Retos
y14 = [1.5, 2.2, 2, 1.7, 2.3]  # Tiempo horas
plt.bar(x30, y30, color='blue', label='Grupo 30')
plt.bar(y30, y14, color='red',  label='Grupo 14')
plt.title('Tiempo de resolucion de retos Misión TIC 2022')
plt.xlabel('Retos')
plt.ylabel('Tiempo (horas)')
plt.legend()
plt.grid()
plt.show()
