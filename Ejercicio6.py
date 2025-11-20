# Ejercicio6.py
from TuringMachine import TuringMachine
import argparse

def copia_cadena(cadena):
    transition_function = {
        # Avanza por toda la cadena hasta el final
        ("q0", "A"): ("q0", "A", "R"),
        ("q0", "B"): ("q0", "B", "R"),
        ("q0", "C"): ("q0", "C", "R"),
        ("q0", "_"): ("q1", "_", "L"),   # cuando llega al blanco, retrocede

        # Estado q1: retroceder hasta el inicio
        ("q1", "A"): ("q1", "A", "L"),
        ("q1", "B"): ("q1", "B", "L"),
        ("q1", "C"): ("q1", "C", "L"),
        ("q1", "_"): ("q2", "_", "R"),   # llegó al inicio, pasa a copiar

        # Estado q2: copiar la cadena al final
        ("q2", "A"): ("q3", "A", "R"),
        ("q2", "B"): ("q4", "B", "R"),
        ("q2", "C"): ("q5", "C", "R"),
        ("q2", "_"): ("qf", "_", "R"),   # fin

        # ---- copiar A ----
        ("q3", "A"): ("q3", "A", "R"),
        ("q3", "B"): ("q3", "B", "R"),
        ("q3", "C"): ("q3", "C", "R"),
        ("q3", "_"): ("q2", "A", "R"),

        # ---- copiar B ----
        ("q4", "A"): ("q4", "A", "R"),
        ("q4", "B"): ("q4", "B", "R"),
        ("q4", "C"): ("q4", "C", "R"),
        ("q4", "_"): ("q2", "B", "R"),

        # ---- copiar C ----
        ("q5", "A"): ("q5", "A", "R"),
        ("q5", "B"): ("q5", "B", "R"),
        ("q5", "C"): ("q5", "C", "R"),
        ("q5", "_"): ("q2", "C", "R"),
    }

    tm = TuringMachine(
        tape=cadena,
        blank="_",
        initial_state="q0",
        final_states={"qf"},
        transition_function=transition_function
    )
    return tm.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejercicio 6: copiar cadena {A,B,C}")
    parser.add_argument("input", nargs="?", default="AABC", help="cadena de entrada (ej: AABC)")
    args = parser.parse_args()
    salida = copia_cadena(args.input)
    print(salida)
