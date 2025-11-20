# Ejercicio7.py
from TuringMachine import TuringMachine
import argparse

def reemplazo_A_por_B(cadena, M=2):
    # Estados: q0 = aún no he reemplazado nada
    #          q1 = ya reemplacé 1
    #          qf = terminé (no reemplazo más)
    transition_function = {
        # Estado q0 (faltan 2 reemplazos)
        ("q0", "A"): ("q1", "B", "R"),   # primera A → B
        ("q0", "B"): ("q0", "B", "R"),   # saltar B
        ("q0", "1"): ("q0", "1", "R"),   # saltar 1
        ("q0", "_"): ("qf", "_", "R"),   # si termina la cadena antes, parar

        # Estado q1 (falta 1 reemplazo)
        ("q1", "A"): ("qf", "B", "R"),   # segunda A → B y luego parar
        ("q1", "B"): ("q1", "B", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "_"): ("qf", "_", "R"),
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
    parser = argparse.ArgumentParser(description="Ejercicio 7: reemplazo de M primeras A's por B's")
    parser.add_argument("input", nargs="?", default="11AAAAB", help="cadena de entrada (ej: 11AAAAB)")
    parser.add_argument("--M", type=int, default=2, help="cantidad de A's a reemplazar (por defecto 2)")
    args = parser.parse_args()
    salida = reemplazo_A_por_B(args.input, args.M)
    print(salida)
