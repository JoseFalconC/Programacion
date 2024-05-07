class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = {}

    def agregar_calificacion(self, materia, calificacion):
        if not isinstance(calificacion, int) or calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe ser un número entero entre 0 y 10.")
        self.calificaciones[materia] = calificacion

    def obtener_info(self):
        info = f"Estudiante: {self.nombre}\nCarrera: {self.carrera}\nCalificaciones:\n"
        for materia, calificacion in self.calificaciones.items():
            info += f"- {materia}: {calificacion}\n"
        return info

class Universidad:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, carrera):
        if not isinstance(nombre, str) or not nombre.isalpha():
            raise ValueError("El nombre del estudiante solo puede contener letras.")
        if carrera not in ["Fisica", "Matematicas", "Mecatronica"]:
            raise ValueError("Carrera no válida.")
        estudiante = Estudiante(nombre, carrera)
        self.estudiantes.append(estudiante)
        return estudiante

    def buscar(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                return estudiante.obtener_info()
        return "El estudiante no fue encontrado."


def solicitar_calificacion():
    while True:
        calificacion = input("Ingrese la calificación (0-10): ")
        try:
            calificacion = int(calificacion)
            if 0 <= calificacion <= 10:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un número entero válido.")

universidad = Universidad()

while True:
    try:
        nombre = input("Ingrese el nombre del estudiante: ")
        while not nombre.isalpha():
            print("El nombre del estudiante solo puede contener letras.")
            nombre = input("Ingrese el nombre del estudiante: ")

        carrera = input("Ingrese la carrera del estudiante (Ciencias físicas, Matemáticas o Mecatrónica): ")
        while carrera not in ["Ciencias físicas", "Matemáticas", "Mecatrónica"]:
            print("Carrera no válida.")
            carrera = input("Ingrese la carrera del estudiante (Ciencias físicas, Matemáticas o Mecatrónica): ")

        estudiante = universidad.agregar_estudiante(nombre, carrera)

        for _ in range(5):  
            materia = input("Ingrese el nombre de la materia: ")
            calificacion = solicitar_calificacion()
            estudiante.agregar_calificacion(materia, calificacion)

        otro_estudiante = input("¿Desea agregar otro estudiante? (Sí/No): ")
        if otro_estudiante.lower() != "sí":
            break
    except ValueError as e:
        print("Error:", e)

for estudiante in universidad.estudiantes:
    print(estudiante.obtener_info())
Busc=input("¿Desea buscar la informacion de algun estudiante?(si/no)").lower()
while Busc=="si":
    nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")
    print(universidad.buscar(nombre_buscar))
    Busc=input("¿Desea buscar la informacion de algun estudiante?(si/no)").lower()
