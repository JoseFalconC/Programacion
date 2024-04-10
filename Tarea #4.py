#Tarea 4. Falcon Cortez Jose de Jesus.

# Hacer un diccionario con el nombre de 10 alumnos de preparatoria con las calificaciones de matematicas...
Diccionario_Calificaciones={}
Diccionario_Calificaciones['Enrique']='8'
Diccionario_Calificaciones['Anyelin Sujey']='10'
Diccionario_Calificaciones['Samantha']='7'
Diccionario_Calificaciones['Grecia']='7'
Diccionario_Calificaciones['Karen']='8'
Diccionario_Calificaciones['Valeria']='9'
Diccionario_Calificaciones['Maryjoce']='7'
Diccionario_Calificaciones['Alma']='8'
Diccionario_Calificaciones['Juan']='9'
Diccionario_Calificaciones['Saul']='7'

#Esto te permite buscar calificaciones en un diccionario 
def buscar_calificacion(diccionario, calificacion_buscar):
    resultados = []
    for nombre, calificacion in diccionario.items():
        if int(calificacion) == int(calificacion_buscar):
            resultados.append((nombre, calificacion))
    return resultados

# Ejemplo de uso
calificacion_deseada = int(input("incerte calificacion a buscar"))  
resultados = buscar_calificacion(Diccionario_Calificaciones, calificacion_deseada)

if resultados:
    print(f"Las personas con calificación {calificacion_deseada} son:")
    for nombre, calificacion in resultados:
        print(f"{nombre}: {calificacion}")
else:
    print(f"No hay personas con calificación {calificacion_deseada}.")
        
    
