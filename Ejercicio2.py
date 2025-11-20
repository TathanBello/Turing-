# Ejercicio2.py
from TuringMachine import TuringMachine
import argparse

def sucesor_unario(cadena):
    # Función de transición:
    # Avanza hasta encontrar el símbolo blanco "_" y ahí escribe un "1".
    transition_function = {
        ("q0", "1"): ("q0", "1", "R"),  # mientras lea 1's sigue avanzando
        ("q0", "_"): ("qf", "1", "R"),  # cuando encuentra blanco, escribe 1 y finaliza
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
    parser = argparse.ArgumentParser(description="Ejercicio 2: sucesor en codificación unaria")
    parser.add_argument("input", nargs="?", default="111", help="cadena unaria de entrada (ej: 111)")
    args = parser.parse_args()
    salida = sucesor_unario(args.input)
    print(salida)
