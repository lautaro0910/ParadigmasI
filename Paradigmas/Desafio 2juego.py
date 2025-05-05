import random

# Opciones 
opciones = ["piedra", "papel", "tijera"]

# Elección del jugador
eleccion_jugador = input("Elige piedra, papel o tijera: ").lower()

# Validar que la elección sea correcta
if eleccion_jugador not in opciones:
    print("Opción no válida.")
else:
    # Elección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)

    # Mostrar las elecciones
    print(f"Tú elegiste: {eleccion_jugador}")
    print(f"La computadora eligió: {eleccion_computadora}")

    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_jugador == "tijera" and eleccion_computadora == "papel") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")