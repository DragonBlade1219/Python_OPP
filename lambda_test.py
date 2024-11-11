# LAMBDAS
def numeros_cuadrados(numero: int) -> int:
    return numero * numero 

numeros = [1, 2, 3, 4]
a = list(map(numeros_cuadrados, numeros))
print(f"Los numeros a los que se le aplicó 'map' son: {numeros} y el resultado es: {a}")

a = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print("\nEl resultado del filtro con lambda es: " + str(a) )

# Suma de dos números:
suma = lambda x, y: x + y
print(suma(5, 3))  # Output: 8

# Multiplicación de un número por 2:
multiplica_por_dos = lambda x: x * 2
print("\nEl resultado de la lambda es: " + str(multiplica_por_dos(4)))  # Output: 8

# Obtener el cuadrado de un número:
cuadrado = lambda x: x ** 2
print("\nEl resultado de la lambda es: " + str(cuadrado(6)))  # Output: 36

# Filtrar números pares de una lista:
lista = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, lista))
print("\nEl resultado del filtro con lambda es: " + str(pares))  # Output: [2, 4, 6]

# Ordenar una lista de tuplas por el segundo elemento:
tuplas = [(1, 2), (3, 1), (5, 4)]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print("\nEl resultado de la lambda para ordernar es: " + str(tuplas_ordenadas))  # Output: [(3, 1), (1, 2), (5, 4)]

#Lambda para convertir una lista de cadenas a mayúsculas:
palabras = ['hola', 'mundo']
mayusculas = list(map(lambda x: x.upper(), palabras))
print("\nEl resultado de la lambda con map es: " + str(mayusculas))  # Output: ['HOLA', 'MUNDO']



#List COMPRENHENSIONS

# Crear una lista de cuadrados:
cuadrados = [x ** 2 for x in range(10)]
print("\nEl resultado de la List Comprenhension es: " + str(cuadrados))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrar números pares de una lista:
pares = [x for x in range(10) if x % 2 == 0]
print("\nEl resultado de la List Comprenhension es: " + str(pares))  # Output: [0, 2, 4, 6, 8]

# Convertir una lista de cadenas a mayúsculas:
palabras = ["hola", "mundo"]
mayusculas = [palabra.upper() for palabra in palabras]
print("\nEl resultado de la List Comprenhension es: " + str(mayusculas))  # Output: ['HOLA', 'MUNDO']

# Crear una lista de tuplas (número, cuadrado):
tuplas = [(x, x ** 2) for x in range(5)]
print("\nEl resultado de la List Comprenhension es: " + str(tuplas))  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Filtrar y transformar una lista de números:
transformados = [x * 2 for x in range(10) if x % 2 != 0]
print("\nEl resultado de la List Comprenhension es: " + str(transformados))  # Output: [2, 6, 10, 14, 18]
