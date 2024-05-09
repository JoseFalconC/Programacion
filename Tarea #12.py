#TAREA 12 FALCON CORTEZ JOSE DE JESUS
#SQLite_SQL, TIFF o GeoTIFF (Datos espaciales o cientificos),Pickle(Formato binario para python)
#Lee todo el contenido del archivo una sola vez
N=[]
with open('D:\\Python\\p.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(linea.strip())
#Tarea separar por espacios, leer numero por numero.
#Para ello se utiliza split
with open('D:\\Python\\p.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        numeros = linea.strip().split()
        for numero in numeros:
            print(numero)
            N.append(numero)
    
#Una lista y cada entrada de estos sea un numero
#strip() se utiliza para eliminar los espacios inicial y final
#split() se utiliza para devolver una lista con separadores los espacios en blanco que los toma como comas en la lista.
##En efecto "numeros" es la lista de numeros:
if N:
    first_number = N[0]
    print(f"{first_number}, primer numero")
else:
    print("La línea está vacía o no contiene números")
