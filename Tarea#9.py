#Tarea crear clase de vectores 2D angulo polar de los vectores,definir ejes coordenados
import math
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def multiply_by_scalar(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def divide_by_scalar(self, scalar):
        if scalar == 0:
            raise ValueError("No se puede dividir por cero.")
        return Vector2D(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return round(math.sqrt(self.x * self.x + self.y * self.y),4)

    def angle_between(self, other):
        dot_product = self * other
        magnitude_product = self.magnitude() * other.magnitude()
        if magnitude_product == 0:
            raise ValueError("No se puede calcular el ángulo con un vector cero.")
        cos_theta = dot_product / magnitude_product
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)
        return round(theta_deg, 2)

    def polar_angle(self):
        if self.x == 0 and self.y == 0:
            raise ValueError("No se puede calcular el ángulo polar de un vector cero.")
        #Este igual se puede determinar con la definicion de producto punto con respecto al vector unitario de la base con direccion en "x_axis"
        return round(math.atan2(self.y, self.x),3)

    def coordinates_in_canonical_basis(self):
        i = Vector2D(1, 0)
        j = Vector2D(0, 1)
        x_coord = self * i
        y_coord = self * j
        return x_coord, y_coord

    def swap_component(self, component, value):
        if component == 'x':
            self.x = value
        elif component == 'y':
            self.y = value
        else:
            print("Componente inválida. Utiliza 'x' o 'y'.")

    def __repr__(self):
        return f"V2D({self.x}, {self.y})"
    def _x_axis_ (scalar):
        i=Vector2D(1,0)
        x_axis=i.multiply_by_scalar(scalar)


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1,"___",v2)
print("Suma:", v1 + v2)
print("Resta:", v1 - v2)
print("Multiplicación por escalar:", v1.multiply_by_scalar(2))
print("Producto punto:", v1 * v2)
print("Magnitud de v1:", v1.magnitude())
print("Ángulo entre v1 y v2:", v1.angle_between(v2))
print("Ángulo polar de v1:", v1.polar_angle())
print("Coordenadas en la base canónica de v1:", v1.coordinates_in_canonical_basis())
v1.swap_component('x', 5)
print("Cambio de componente:", v1)
