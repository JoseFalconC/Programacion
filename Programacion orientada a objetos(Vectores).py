import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def multiply_by_scalar(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def divide_by_scalar(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def vector(self, other1, other2):
        elem = other1.cross_product(other2).multiply_by_scalar(other1.cross_product(other2).magnitude()) - other2.cross_product(other1).multiply_by_scalar(other2.cross_product(other1).magnitude())
        return elem

    def norma(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def angulo_vectores(self, other):
        angulo = math.acos(self * other / (self.norma() * other.norma())) * 180 / 3.1416
        return round(angulo, 2)

    def swap_component(self, component, value):
        if component == 'x':
            self.x = value
        elif component == 'y':
            self.y = value
        elif component == 'z':
            self.z = value
        else:
            print("Componente inválida. Utiliza 'x', 'y' o 'z'.")

    def __repr__(self):
        return f"V3D({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
v3 = Vector3D(7,  8, 9)

# Suma de vectores
sum_result = v1 + v2
print("Suma de vectores:", sum_result)

# Resta de vectores
sub_result = v1 - v2
print("Resta de vectores:", sub_result)

# Multiplicación por escalar
scalar_multiplication = v1.multiply_by_scalar(3)
print("Multiplicación por escalar:", scalar_multiplication)

# Producto punto
dot_product = v1 * v2
print("Producto punto:", dot_product)

# Producto cruz
cross_product = v1.cross_product(v2)
print("Producto cruz:", cross_product)

# Norma del vector
norma1 = v1.norma()
print("Norma del vector:", norma1)

# Ángulo entre vectores
v5 = Vector3D(0, 1, 0)
v6 = Vector3D(1, 1, 0)
ang = v5.angulo_vectores(v6)
print("Ángulo entre vectores:", ang)

# Triple producto vectorial
gauss = v1.vector(v2, v3)
print("Triple producto vectorial:", round(gauss.x, 2), round(gauss.y, 2), round(gauss.z, 2))

# División de un vector por un escalar
scalar = 2
div_by_scalar_result = v1.divide_by_scalar(scalar)
print("División de un vector por un escalar:", div_by_scalar_result, "escalar:",scalar)

# Modificar componente
print("Vector original:", v1)
v1.swap_component('x', 3)
print("Nuevo vector v1:", v1)


