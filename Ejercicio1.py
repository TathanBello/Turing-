# Ejercicio1.py
from TuringMachine import TuringMachine
import argparse

def complemento_binario(cadena):
    transition_function = {
        ("q0", "0"): ("q0", "1", "R"),
        ("q0", "1"): ("q0", "0", "R"),
        ("q0", "_"): ("qf", "_", "R"),
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
    parser = argparse.ArgumentParser(description="Ejercicio 1: complemento a 1 de un número binario")
    parser.add_argument("input", nargs="?", default="10101", help="cadena binaria de entrada (ej: 10101)")
    args = parser.parse_args()
    salida = complemento_binario(args.input)
    print(salida)
