import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.quantum_info.operators import Operator
from qiskit import Aer
from qiskit_aer import AerSimulator

import board
import pieces

class Chess: 

    def __init__(self):
        self.board = board.Board()

def main():
    chess = Chess()
    chess.board.print_board()


if __name__ == "__main__":
    main()