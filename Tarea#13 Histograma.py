import random

# Generar 50 números aleatorios entre 0 y 10
numeros_50 = [random.randint(0, 10) for _ in range(50)]

rango_1 = [num for num in numeros_50 if num < 2]
rango_2 = [num for num in numeros_50 if 2 <= num < 4]
rango_3 = [num for num in numeros_50 if 4 <= num < 6]
rango_4 = [num for num in numeros_50 if 6 <= num < 8]
rango_5 = [num for num in numeros_50 if 8 <= num <= 10]


print("Números generados:", numeros_50)
print("Rango 1 (< 2):", rango_1)
print("Rango 2 (>= 2 y < 4):", rango_2)
print("Rango 3 (>= 4 y < 6):", rango_3)
print("Rango 4 (>= 6 y < 8):", rango_4)
print("Rango 5 (>= 8 y <= 10):", rango_5)

# Generar 1000 números aleatorios entre 0 y 10
numeros_1000 = [random.randint(0, 10) for _ in range(1000)]


rango_1 = [num for num in numeros_1000 if num < 2]
rango_2 = [num for num in numeros_1000 if 2 <= num < 4]
rango_3 = [num for num in numeros_1000 if 4 <= num < 6]
rango_4 = [num for num in numeros_1000 if 6 <= num < 8]
rango_5 = [num for num in numeros_1000 if 8 <= num <= 10]

print("Números generados:", numeros_1000)
print("Rango 1 (< 2):", rango_1)
print("Rango 2 (>= 2 y < 4):", rango_2)
print("Rango 3 (>= 4 y < 6):", rango_3)
print("Rango 4 (>= 6 y < 8):", rango_4)
print("Rango 5 (>= 8 y <= 10):", rango_5)
import matplotlib.pyplot as plt

rangos = ['Rango 1', 'Rango 2', 'Rango 3', 'Rango 4', 'Rango 5']
frecuencias = [len(rango_1), len(rango_2), len(rango_3), len(rango_4), len(rango_5)]

plt.bar(rangos, frecuencias, color='skyblue')

plt.xlabel('Rangos')
plt.ylabel('Frecuencia')
plt.title('Histograma de 50 números aleatorios')

plt.show()
import matplotlib.pyplot as plt


rangos = ['Rango 1', 'Rango 2', 'Rango 3', 'Rango 4', 'Rango 5']
frecuencias = [len(rango_1), len(rango_2), len(rango_3), len(rango_4), len(rango_5)]


plt.bar(rangos, frecuencias, color='lightgreen')

plt.xlabel('Rangos')
plt.ylabel('Frecuencia')
plt.title('Histograma de 1000 números aleatorios')


plt.show()

