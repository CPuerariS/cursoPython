#-Que se pueda jugar correctamente. 
#-Que el programa pueda finalizar sin errores.
#-Esta unicamnte permitido utilizar estas funciones: -> print(), input(), len(), range(), append(),extend(),insert(),pop() y funciones propias.
#- Se puede utilizar cualquier tipo de ciclos, y condiciones.

def mostrar_tablero(tablero):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(tablero[i][j], "|", end=" ")
        print("\n-------------")

def jugar_tateti():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    while True:
        mostrar_tablero(tablero)

        fila = int(input("Elige una fila (0-2): "))
        columna = int(input("Elige una columna (0-2): "))

        if tablero[fila][columna] != " ":
            print("Esa posición ya está ocupada. Intenta nuevamente.")
            continue

        tablero[fila][columna] = jugador_actual

        # Verificar ganador
        if (tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador_actual or
            tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador_actual or
            tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador_actual or
            tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador_actual):
            mostrar_tablero(tablero)
            print("¡Felicidades! El jugador", jugador_actual, "ha ganado.")
            break

        # Verificar empate
        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            mostrar_tablero(tablero)
            print("¡Es un empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar_tateti()

