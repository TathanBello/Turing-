# Ejercicio3.py
from TuringMachine import TuringMachine
import argparse

def predecesor_unario(cadena):
    # La máquina recorre todos los "1" hasta encontrar un blanco "_".
    # Luego retrocede un paso y borra el último "1" -> lo reemplaza por "_".
    transition_function = {
        ("q0", "1"): ("q0", "1", "R"),   # seguir avanzando sobre los 1
        ("q0", "_"): ("q1", "_", "L"),   # al llegar al final, mover a la izquierda
        ("q1", "1"): ("qf", "_", "R"),   # borrar el último "1" y terminar
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
    parser = argparse.ArgumentParser(description="Ejercicio 3: predecesor en codificación unaria")
    parser.add_argument("input", nargs="?", default="1111", help="cadena unaria de entrada (ej: 1111)")
    args = parser.parse_args()
    salida = predecesor_unario(args.input)
    print(salida)
