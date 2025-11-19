# Ejercicio10.py
from TuringMachine import TuringMachine
import argparse

def antecesor_binario(cadena):
    transition_function = {
        # q0: mover cabeza hasta el final de la cadena
        ("q0", "0"): ("q0", "0", "R"),
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "_"): ("q1", "_", "L"),   # al llegar al blanco, retrocedemos

        # q1: intentar restar 1 (manejo del préstamo)
        ("q1", "1"): ("qf", "0", "R"),   # si vemos 1 → lo cambiamos a 0 y fin
        ("q1", "0"): ("q1", "1", "L"),   # si vemos 0 → lo cambiamos a 1 y seguimos pidiendo préstamo
        ("q1", "_"): ("qf", "_", "R"),   # si llegamos al inicio → fin (ya no hay más que restar)
    }

    tm = TuringMachine(
        tape=cadena,
        blank="_",
        initial_state="q0",
        final_states={"qf"},
        transition_function=transition_function
    )
    resultado = tm.run()
    # Eliminar ceros iniciales innecesarios
    return resultado.lstrip("0") or "0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejercicio 10: antecesor de un número binario")
    parser.add_argument("input", nargs="?", default="1100", help="cadena binaria de entrada (ej: 1100)")
    args = parser.parse_args()
    salida = antecesor_binario(args.input)
    print(salida)
