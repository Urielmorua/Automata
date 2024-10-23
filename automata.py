# Definimos un autómata con tres estados
class Automata:
    def __init__(self):
        # Estados: q0, q1, q2
        self.state = 'q0'  # Estado inicial
        self.final_states = {'q2'}  # Estado final
        # Transiciones: (estado_actual, simbolo) -> estado_siguiente
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q1',
            ('q0', 'c'): 'q2',
            ('q1', 'a'): 'q0',
            ('q1', 'b'): 'q0',
            ('q1', 'c'): 'q2',
            ('q2', 'a'): 'q1',
            ('q2', 'b'): 'q1',
            ('q2', 'c'): 'q2',
        }

    # Función para procesar la cadena
    def process(self, string):
        for char in string:
            if (self.state, char) in self.transitions:
                self.state = self.transitions[(self.state, char)]
            else:
                return False  # Si encuentra un símbolo inválido, rechaza la cadena

        # Verifica si termina en un estado final
        return self.state in self.final_states

# Prueba del autómata
automata = Automata()

# Introduce la cadena que deseas procesar
cadena = input("Introduce una cadena (compuesta por 'a', 'b', 'c'): ")

# Procesa la cadena
if automata.process(cadena):
    print("Cadena aceptada.")
else:
    print("Cadena rechazada.")
