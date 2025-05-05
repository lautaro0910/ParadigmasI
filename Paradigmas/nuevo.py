import turtle

t = turtle.Turtle()
t.shape("turtle")   # Cambia la forma a tortuga
t.speed(2)          # Velocidad moderadamente lenta

for _ in range(4):
    t.forward(100)  # Lado del cuadrado
    t.right(90)     # Gira 90° a la derecha
