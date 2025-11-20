# Ejercicio4.py
from TuringMachine import TuringMachine
import argparse

def paridad_binaria(cadena):
    # q0 = paridad par
    # q1 = paridad impar
    transition_function = {
        # Leer 0 → no cambia paridad
        ("q0", "0"): ("q0", "0", "R"),
        ("q1", "0"): ("q1", "0", "R"),

        # Leer 1 → cambia paridad
        ("q0", "1"): ("q1", "1", "R"),
        ("q1", "1"): ("q0", "1", "R"),

        # Fin de la cadena
        ("q0", "_"): ("qf", "0", "R"),  # si par → añade 0
        ("q1", "_"): ("qf", "1", "R"),  # si impar → añade 1
    }

    tm = TuringMachine(
        tape=cadena,
        blank="_",
        initial_state="q0",   # empezamos suponiendo paridad "0"
        final_states={"qf"},
        transition_function=transition_function
    )
    return tm.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejercicio 4: paridad de un número binario")
    parser.add_argument("input", nargs="?", default="1011", help="cadena binaria de entrada (ej: 1011)")
    args = parser.parse_args()
    salida = paridad_binaria(args.input)
    print(salida)
