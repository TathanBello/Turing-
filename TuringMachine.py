# TuringMachine.py
"""
Clase TuringMachine reutilizable para los ejercicios del PDF.
No debe ejecutar nada al importarse (no tiene código fuera de funciones/clases).
"""

class TuringMachine:
    def __init__(self, tape="", blank="_", initial_state="q0", final_states=None, transition_function=None):
        self.blank = blank
        self.tape = list(tape) if tape != "" else [blank]
        self.head = 0
        self.state = initial_state
        self.final_states = set(final_states or [])
        self.transition_function = transition_function or {}

    def _read(self):
        if 0 <= self.head < len(self.tape):
            return self.tape[self.head]
        return self.blank

    def _write(self, symbol):
        if 0 <= self.head < len(self.tape):
            self.tape[self.head] = symbol
        elif self.head == len(self.tape):
            self.tape.append(symbol)
        else:
            # si la cabeza está fuera a la izquierda, insertamos
            while self.head < 0:
                self.tape.insert(0, self.blank)
                self.head += 1
            if self.head == len(self.tape):
                self.tape.append(symbol)
            else:
                self.tape[self.head] = symbol

    def step(self):
        symbol = self._read()
        key = (self.state, symbol)
        if key not in self.transition_function:
            # No hay transición: detenemos la máquina
            self.state = None
            return False
        new_state, write_symbol, direction = self.transition_function[key]
        self._write(write_symbol)
        if direction == "R":
            self.head += 1
            if self.head == len(self.tape):
                self.tape.append(self.blank)
        elif direction == "L":
            self.head -= 1
            if self.head < 0:
                # extendemos a la izquierda
                self.tape.insert(0, self.blank)
                self.head = 0
        else:
            raise ValueError("La dirección debe ser 'R' o 'L'")
        self.state = new_state
        return True

    def run(self, max_steps=10000):
        steps = 0
        while self.state is not None and self.state not in self.final_states and steps < max_steps:
            ok = self.step()
            if not ok:
                break
            steps += 1
        return self.get_tape_str()

    def get_tape_str(self):
        s = "".join(self.tape)
        return s.strip(self.blank)
