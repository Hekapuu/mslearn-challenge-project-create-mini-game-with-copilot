#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")


import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    puntaje = {"jugador": 0, "oponente": 0}

    def resultado_ronda(jugador, oponente):
        if jugador == oponente:
            return "Empate"
        elif (
            (jugador == "piedra" and oponente == "tijera")
            or (jugador == "tijera" and oponente == "papel")
            or (jugador == "papel" and oponente == "piedra")
        ):
            puntaje["jugador"] += 1
            return "¡Ganaste!"
        else:
            puntaje["oponente"] += 1
            return "¡Perdiste!"

    while True:
        print("\nElige: piedra, papel o tijera. Para salir, escribe 'salir'.")
        eleccion_jugador = input().lower()

        if eleccion_jugador == "salir":
            break
        elif eleccion_jugador not in opciones:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")
            continue

        eleccion_oponente = random.choice(opciones)
        print(f"\nOponente elige: {eleccion_oponente}")

        resultado = resultado_ronda(eleccion_jugador, eleccion_oponente)
        print(f"\n{resultado}")
        print(f"Puntaje: Jugador {puntaje['jugador']} - {puntaje['oponente']} Oponente")

    print("\nJuego terminado. ¡Hasta luego!")

# Inicia el minijuego
jugar_piedra_papel_tijera()

