# Ejercicio5.py
from TuringMachine import TuringMachine
import argparse

def contador_unario(cadena):
    transition_function = {
        # Si encuentra 'a', 'b' o 'c' → borrar y pasar a estado q1 para ir al final
        ("q0", "a"): ("q1", "_", "R"),
        ("q0", "b"): ("q1", "_", "R"),
        ("q0", "c"): ("q1", "_", "R"),

        # Estado q1 → moverse a la derecha hasta encontrar el blanco
        ("q1", "a"): ("q1", "a", "R"),
        ("q1", "b"): ("q1", "b", "R"),
        ("q1", "c"): ("q1", "c", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "_"): ("q2", "1", "L"),   # cuando encuentra blanco, escribe 1 y retrocede

        # Estado q2 → regresar al inicio para buscar más símbolos
        ("q2", "a"): ("q2", "a", "L"),
        ("q2", "b"): ("q2", "b", "L"),
        ("q2", "c"): ("q2", "c", "L"),
        ("q2", "1"): ("q2", "1", "L"),
        ("q2", "_"): ("q0", "_", "R"),   # al llegar al inicio vuelve a q0

        # Cuando ya no hay más símbolos a procesar → detenerse
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
    parser = argparse.ArgumentParser(description="Ejercicio 5: contador unario de caracteres {a,b,c}")
    parser.add_argument("input", nargs="?", default="abca", help="cadena de entrada (ej: abca)")
    args = parser.parse_args()
    salida = contador_unario(args.input)
    print(salida)
