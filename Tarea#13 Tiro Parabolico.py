import turtle
import math
import time

#x=vcos(theta)*t
def posicion_x(t, velocidad_inicial, angulo):
    return velocidad_inicial * math.cos(math.radians(angulo)) * t

#y=vsin(theta)*t-1/2(g)*t**2
def posicion_y(t, velocidad_inicial, angulo, gravedad):
    return velocidad_inicial * math.sin(math.radians(angulo)) * t - 0.5 * gravedad * t**2

def dibujar_tiro_parabolico(velocidad_inicial, angulo, gravedad):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.setworldcoordinates(0, 0, 100, 80)

    t = 0
    tortuga = turtle.Turtle()
    tortuga.penup()
    tortuga.goto(0, 0)
    tortuga.pendown()

    while True:
        x = posicion_x(t, velocidad_inicial, angulo)
        y = posicion_y(t, velocidad_inicial, angulo, gravedad)
        
        if y >= 0: 
            tortuga.goto(x, y)
            tortuga.dot(5) 
        else:
            break  
        
        t += 0.1  

    time.sleep(5)  
    turtle.done()

#Parametros de velocidad,angulo y aceleracion local gravitatoria.
velocidad_inicial=30  
angulo = 45  
gravedad = 9.8  

dibujar_tiro_parabolico(velocidad_inicial, angulo, gravedad)
