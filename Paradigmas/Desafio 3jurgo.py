import random

palabras = ["python", "java", "desarrollador", "programacion", "algoritmo", "computadora", "redes"]

def jugar():
    print("¡Bienvenido al juego del Ahorcado!")

 
    palabra_secreta = random.choice(palabras)
    palabra_oculta = ["_"] * len(palabra_secreta)
    intentos_maximos = 6  
    intentos_fallidos = 0
    letras_adivinadas = []

    # Bucle principal del juego
    while intentos_fallidos < intentos_maximos:
        print("\nPalabra: " + " ".join(palabra_oculta))
        print(f"Intentos restantes: {intentos_maximos - intentos_fallidos}")
        letra = input("Ingresa una letra: ").lower()

        # Verificamos si la letra es válida
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra válida.")
            continue

        # Añadimos la letra a las adivinadas
        letras_adivinadas.append(letra)

        # Verificamos si la letra está en la palabra secreta
        if letra in palabra_secreta:
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else:
            intentos_fallidos += 1
            print(f"¡La letra '{letra}' no está en la palabra!")

        # Verificamos si el jugador ha adivinado la palabra
        if "_" not in palabra_oculta:
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

    # Si se alcanzan los intentos máximos, el jugador pierde
    if intentos_fallidos == intentos_maximos:
        print(f"\n¡Has perdido! La palabra era: {palabra_secreta}")

    # Preguntar si quiere jugar nuevamente
    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if jugar_nuevamente == 's':
        jugar()
    else:
        print("¡Gracias por jugar! Hasta la próxima.")

jugar()

