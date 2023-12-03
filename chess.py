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

        self.turn = "white"

def main():
    chess = Chess()
    chess.board.print_board()

    # Create Quantum Circuit
    qr = QuantumRegister(20, 'q')
    anc = QuantumRegister(1, 'ancilla')
    cr = ClassicalRegister(1, 'c')
    circ = QuantumCircuit(qr, anc, cr)

    # Flip qubits representing pieces to 1
    for row in range(5):
        for col in range(4):
            if chess.board.board[row][col] != None:
                circ.x(qr[row*4 + col])
    
    # Loop for user input
    while True:
        print("Turn: " + chess.turn)
        start = board.alphanum_to_index(input("From: "))
        end = board.alphanum_to_index(input("To: "))
        
        # Check if input is valid: Length is either start, end 1, start 2 end 1, or start 1 end 2
        if len(start) == 1 and len(end) == 1:
            start = start[0]
            end = end[0]
        elif len(start) == 2 and len(end) == 1: # Merge Move
            start = start[0]
            end = end[0]
        elif len(start) == 1 and len(end) == 2: # Split Move
            start = start[0]
            end = end[0]
        else:
            print("Invalid input")
            continue

        


if __name__ == "__main__":
    main()