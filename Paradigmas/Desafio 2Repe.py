def imprimir_tablero(ancho, alto):
    cuadrado_verde = "🟩"  # (Cuadrado verde)
    cuadrado_blanco = "⬜" # Cuadrado blanco)

    for fila in range(alto):
        for columna in range(ancho):
            if (fila + columna) % 2 == 0:
                print(cuadrado_verde, end=" ")
            else:
                print(cuadrado_blanco, end=" ")
        print() 

tamano_ancho = 8
tamano_alto = 6

# Llamar a la función
imprimir_tablero(tamano_ancho, tamano_alto)
