import random

numero_secreto = random.randint(1, 10)

intentos = 0

print("¡Bienvenido al juego de Adivina el Número!")

# Inicia el ciclo para que el jugador intente adivinar
while True:
    # Solicita un número al jugador
    numero_usuario = int(input("Ingresa un número entre 1 y 10: "))

    # Convierte la entrada del jugador en un número entero
    numero_usuario = int(numero_usuario)

    # Verifica si el número está en el rango permitido
    if numero_usuario < 1 or numero_usuario > 10:
        print("El número debe estar entre 1 y 10.")
        continue

    intentos += 1

    if numero_usuario < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif numero_usuario > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
