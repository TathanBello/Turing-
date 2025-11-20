# Ejercicio9.py
from TuringMachine import TuringMachine
import argparse

def sucesor_binario(cadena):
    transition_function = {
        # q0: mover cabeza hasta el final de la cadena
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "_"): ("q1", "_", "L"),   # al llegar al blanco, retrocedemos

        # q1: intentar sumar 1 (manejo de acarreo)
        ("q1", "0"): ("qf", "1", "R"),   # si vemos 0, lo cambiamos a 1 → fin
        ("q1", "1"): ("q1", "0", "L"),   # si vemos 1, lo cambiamos a 0 y seguimos a la izquierda
        ("q1", "_"): ("qf", "1", "R"),   # si llegamos al inicio, agregamos un 1 extra → fin
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
    parser = argparse.ArgumentParser(description="Ejercicio 9: sucesor de un número binario")
    parser.add_argument("input", nargs="?", default="1011", help="cadena binaria de entrada (ej: 1011)")
    args = parser.parse_args()
    salida = sucesor_binario(args.input)
    print(salida)
