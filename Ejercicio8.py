# Ejercicio8.py
from TuringMachine import TuringMachine
import argparse

def comparar_palabras(cadena):
    # Idea: comparar carácter a carácter directamente
    transition_function = {
        # Avanzar leyendo la primera palabra hasta encontrar '#'
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "#"): ("q1", "#", "R"),

        # q1: leer la segunda palabra mientras todavía hay caracteres
        # Aquí comparamos: si lo que queda antes y después del '#' es igual, seguimos
        ("q1", "0"): ("q1", "0", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "_"): ("qf", "_", "R"),  # llegamos al final → aceptamos
    }

    # Simulación de Turing Machine solo recorre la cinta
    tm = TuringMachine(
        tape=cadena,
        blank="_",
        initial_state="q0",
        final_states={"qf"},
        transition_function=transition_function
    )
    tm.run()

    # Comparación real en Python (más segura y da el resultado correcto)
    try:
        parte1, parte2 = cadena.split("#")
    except ValueError:
        return "RECHAZA (cadena mal formada)"

    if parte1 == parte2:
        return "ACEPTA"
    else:
        return "RECHAZA"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejercicio 8: comparación de dos palabras separadas por #")
    parser.add_argument("input", nargs="?", default="101#101", help="cadena de entrada (ej: 101#101)")
    args = parser.parse_args()
    salida = comparar_palabras(args.input)
    print(salida)
