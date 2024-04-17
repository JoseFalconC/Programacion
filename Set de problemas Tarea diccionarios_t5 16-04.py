
#Set de problemas Tarea diccionarios_t5 16-04

#1 Escribe un programa en Python para multiplicar todos los elementos de un diccionario.
#Para multiplicar los elementos de un diccionario, definamos una funcion que te añada numeros a un diccionario.def multiplicar_diccionario(diccionario):
def multiplicar_diccionario(diccionario):
    resultado = 1
    for valor in diccionario.values():
        resultado *= valor
    return resultado


mi_diccionario = {'a': 2, 'b': 3, 'c': 4}

resultado_multiplicacion = multiplicar_diccionario(mi_diccionario)

print("El resultado de la multiplicación de todos los valores del diccionario es:", resultado_multiplicacion)

#2 Escribe un programa en Python para eliminar una clave de un diccionario.
#Se define una funcion eliminar con la operacion del:
def eliminar_clave(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
        print("Clave eliminada con éxito.")
    else:
        print("La clave especificada no existe en el diccionario.")

mi_diccionario = {'agua': 2, 'betta': 3, 'cocos': 4}

clave_a_eliminar = 'betta'
eliminar_clave(mi_diccionario, clave_a_eliminar)

print("Diccionario después de eliminar la clave:", mi_diccionario)

#3 Escribe un programa en Python para convertir dos listas en un diccionario.
#Empleamos la operacion dpredefinida zip para unir en pares y luego usar dict para convertirlo a diccionario
def listas_a_diccionario(lista_claves, lista_valores):
    if len(lista_claves) != len(lista_valores):
        print("Las listas deben tener la misma longitud.")
        return None
    else:
        return dict(zip(lista_claves, lista_valores))

claves = ['a', 'b', 'c']
valores = [1, 2, 3]

mi_diccionario = listas_a_diccionario(claves, valores)

print("Diccionario resultante:", mi_diccionario)

#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
def ordenar_por_clave(diccionario):
    diccionario_ordenado = dict(sorted(diccionario.items()))
    return diccionario_ordenado

mi_diccionario = {'b': 2, 'c': 3, 'a': 1}

diccionario_ordenado = ordenar_por_clave(mi_diccionario)

print("Diccionario ordenado por clave:", diccionario_ordenado)


#5 Escribe un programa en Python para obtener los valores máximo y mínimo de un diccionario.
#Simplemente es emplear la operacion predefinida max y min sobre la cadena
#Primera forma:
def obtener_valor_maximo(diccionario):
    if len(diccionario) == 0:
        return None
    return max(diccionario.values())

def obtener_valor_minimo(diccionario):
    if len(diccionario) == 0:
        return None
    return min(diccionario.values())

mi_diccionario = {'a': 10, 'b': 5, 'c': 20}


valor_maximo = obtener_valor_maximo(mi_diccionario)
valor_minimo = obtener_valor_minimo(mi_diccionario)

print("Valor máximo del diccionario:", valor_maximo)
print("Valor mínimo del diccionario:", valor_minimo)
#Segunda forma:

def valor_max(diccionario):
    lista = []
    for llave, elemento in diccionario.items():
        lista.append(elemento)
    return max(lista)

def valor_min(diccionario):
    lista = []
    for llave, elemento in diccionario.items():
        lista.append(elemento)
    return min(lista)


mi_diccionario = {'a': 10, 'b': 5, 'c': 20}


valor_maxi = valor_max(mi_diccionario)
valor_mini = valor_min(mi_diccionario)

print("Valor máximo del diccionario:", valor_maxi)
print("Valor mínimo del diccionario:", valor_mini)


        
    

#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad


persona = Persona("Juan", 30, "Ciudad de México")

diccionario_persona = vars(persona)
#Vars retorna los atributos como diccionario.

print("Diccionario creado a partir de los campos del objeto Persona:")
print(diccionario_persona)

#7 Escribe un programa en Python para eliminar duplicados del diccionario.
#Supongamos que el duplicado es en la llave del diccionario, entonces definimos una funcion para eliminar ese duplicado.
def eliminar_duplicados_clave(diccionario):
    diccionario_unico = {}
    for clave, valor in diccionario.items():
        if clave not in diccionario_unico:
            diccionario_unico[clave] = valor
    return diccionario_unico

mi_diccionario = {'a': 1, 'b': 2, 'a': 3}
diccionario_sin_duplicados = eliminar_duplicados_clave(mi_diccionario)
print(diccionario_sin_duplicados)
#El problema de esta funcion definida es que lo hara de forma ordenada.




#8 Escribe un programa en Python para verificar si un diccionario está vacío o no.
#Simplemente se necesita la medida de sus elementos:
mi_diccionario = {}  
if len(mi_diccionario) != 0:
    print("El diccionario no está vacío.")
else:
    print("El diccionario está vacío.")

#9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios. Diccionario original: [{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 10 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias [92, 94, 88] Diccionario original: [{'matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 11 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas [90, 89, 92]

diccionarios = [{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]


valores_ciencia = [diccionario['ciencia'] for diccionario in diccionarios if 'ciencia' in diccionario]
print("Valores correspondientes a Ciencia:", valores_ciencia)

valores_matematicas = [diccionario['Matematicas'] for diccionario in diccionarios if 'Matematicas' in diccionario]
print("Valores correspondientes a Matemáticas:", valores_matematicas)
#Esto extrae los valores en una lista comprimida, iterando en la lista y accediendo al elemento del diccionario

#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.
#Se emplea el metodo values para obtener una lista de los elementos del dicionario y se mide con len, esto debido a que en un diccionario, cada objeto esta acompañado de una llave
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

valores = mi_diccionario.values()
longitud_diccionario_valores = len(valores)

print("La longitud del diccionario de valores es:", longitud_diccionario_valores)
#13 Escribe un programa en Python para obtener la profundidad de un diccionario.
#Referido al nivel maximo de anidamiento de un diccionario:
#Con isinstance se verifica si el objeto referido es de la misma clase .
def profundidad_diccionario(diccionario):
    if not isinstance(diccionario, dict):
        return 0
    if not diccionario:
        return 1
    return 1 + max(profundidad_diccionario(valor) for valor in diccionario.values())


mi_diccionario = {'a': {'b': {'c': {'d': 1}}}, 'e': 2}

profundidad = profundidad_diccionario(mi_diccionario)
print("La profundidad del diccionario es:", profundidad)

#14 Escribe un programa en Python para acceder al elemento de la clave de un diccionario por índice. Salida esperada: física matemáticas química
#Para este se puede emplear el .keys()
mi_diccionario = {'física': 90, 'matemáticas': 95, 'química': 88}
claves = list(mi_diccionario.keys())
print(claves)
#Otra forma:
def llaves(diccionario):
    lista=[]
    for llaves in diccionario:
        lista.append(llaves)
    return lista
mi_diccionario = {'física': 90, 'matemáticas': 95, 'química': 88}
print(llaves(mi_diccionario))

#15 Escribe un programa en Python para convertir un diccionario en una lista de listas. Diccionario original: {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'} Convierte el mencionado diccionario en una lista de listas: [[1, 'rojo'], [2, 'verde'], [3, 'negro'], [4, 'blanco'], [5, 'negro']]
diccionario_original = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
lista_de_listas = [[clave, valor] for clave, valor in diccionario_original.items()]
#Se emplea el .items() para acceder a la llave y al valor
print(lista_de_listas)

#Otra forma:
def lista(diccionario):
    lista = []
    for clave, valor in diccionario.items():
        lista.append([clave, valor])
    return lista

diccionario_original = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}
resultado = lista(diccionario_original)
print(resultado)
     
#16 Escribe un programa en Python para filtrar números pares de un diccionario de valores. Diccionario original: {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]} Filtra números pares de los valores del diccionario mencionado: {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]} Diccionario original: {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]} Filtra números pares de los valores del diccionario mencionado: {'V': [], 'VI': [], 'VII': [2]}
def filtrar_pares(diccionario):
#Esto te permite iterar en los valores y comparar en modulo en una lista comprimida
    diccionario_filtrado = {clave: [valor for valor in valores if valor % 2 == 0] for clave, valores in diccionario.items()}
    return diccionario_filtrado

diccionario_original1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
diccionario_original2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

diccionario_filtrado1 = filtrar_pares(diccionario_original1)
diccionario_filtrado2 = filtrar_pares(diccionario_original2)

print("Diccionario original 1:", diccionario_original1)
print("Diccionario filtrado 1:", diccionario_filtrado1)
print("Diccionario original 2:", diccionario_original2)
print("Diccionario filtrado 2:", diccionario_filtrado2)
