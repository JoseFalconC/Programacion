class Alumno:
    def __init__(self, nombre, licenciatura, grupo):
        self.nombre = nombre
        self.licenciatura = licenciatura
        self.grupo = grupo
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_nombre(self):
        return self.nombre

class LicenciaturaFisica(Alumno):
    def __init__(self, nombre, grupo):
        super().__init__(nombre, "Física", grupo)

class LicenciaturaMatematicas(Alumno):
    def __init__(self, nombre, grupo):
        super().__init__(nombre, "Matemáticas", grupo)

class LicenciaturaElectronica(Alumno):
    def __init__(self, nombre, grupo):
        super().__init__(nombre, "Electrónica", grupo)


materias_fisica = ["Mecánica Clásica", "Electromagnetismo", "Mecánica Cuántica","Relatividad General","Gravitacion"]
materias_matematicas = ["Cálculo I", "Álgebra Lineal", "Geometría Diferencial","Topologia","Analisis estadistico"]
materias_electronica = ["Circuitos Eléctricos", "Electrónica Analógica", "Electrónica Digital","Analisis complejo","Fisica de circuitos"]

nombres_alumnos = [
    "Mary Joce", "Anyelin", "Karen Valenzuela", "Luis Alberto", "Carlos Lopez",
    "Laura Sanchez", "David Rodriguez", "Sofia Hernandez", "Javier Diaz", "Elena Fernandez"
]

alumnos = []
for i, nombre in enumerate(nombres_alumnos):
    grupo = i // 3 + 1  
    if i < 3:
        alumno = LicenciaturaFisica(nombre, grupo)
        for materia in materias_fisica:
            alumno.agregar_materia(materia)
    elif i < 6:
        alumno = LicenciaturaMatematicas(nombre, grupo)
        for materia in materias_matematicas:
            alumno.agregar_materia(materia)
    else:
        alumno = LicenciaturaElectronica(nombre, grupo)
        for materia in materias_electronica:
            alumno.agregar_materia(materia)
    alumnos.append(alumno)

for alumno in alumnos:
    print(f"Nombre: {alumno.obtener_nombre()}")
    print(f"Licenciatura: {alumno.licenciatura}")
    print(f"Grupo: {alumno.grupo}")
    print("Materias:")
    for materia in alumno.materias:
        print(f"- {materia}")
    print()

