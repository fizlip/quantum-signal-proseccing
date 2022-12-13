import sys
import math

from qsp_operation import Evaluate, PlotResponse

from angle_sequence import QuantumSignalProcessingPhases
from response import PlotQSPResponse 
from poly import StringPolynomial

from remez import Remez

def main():
    '''
    Main function. Commands with corresponding arguments. 
    '''

    help_text = """
    Quantum Signal Processing for seminar Advanced Topics of Quantum Computing [IN2107]

    usage: main.py cmd args
    Commands:
        qsp_seq - compute the QSP sequence for a set of phase angles and plot the result
        qsp - compute the phase angles for given polynomial and plot the result
    Examples:
        main.py -qsp_seq 1,1,1,1
        main.py -qsp_seq bb1
        main.py -qsp 'x**2'
        main.py -qsp 'np.cos(x**2)'
    """

    args = sys.argv[1:]
    cmd = args[0][1:]
    arg = args[1:]

    if (cmd == "help"):
        print(help_text)

    if(cmd == "qsp_seq"):

        if(arg[0] == "bb1"):
            eta = 0.5*math.acos(-0.25)
            phis = [math.pi/2, -eta, 2*eta, 0, -2*eta, eta]
        else:
            phis = [int(i) for i in arg[0].split(",")]

        print(f"[main.py] Evaluating QSP sequence for: {phis}")
        data = Evaluate(phis)
        PlotResponse(data)

    if(cmd == "qsp"):

        print(f"[main.py] Calculating phis for: {arg[0]}") 

        # Change degree of polynomial by passing an extra argument. 
        if(len(arg) == 2):
            poly = StringPolynomial(arg[0], arg[1])
        else:
            poly = StringPolynomial(arg[0], 10)
         
        # Here we use TensorFlor 'tf' to approximate phases
        ang_seq = QuantumSignalProcessingPhases(poly, method="tf")

        # This function plots the approximated polynomial and compares it to target
        PlotQSPResponse(ang_seq, target=poly, signal_operator="Wx")
    if(cmd == "qsp_remez"):
        print(f"[main.py] Calculating phis using Remez for: {arg[0]}") 
        poly = StringPolynomial(arg[0], 10)
        ang_seq = Remez(poly, 1) 

        print(f"Angle sequqnce as calculated by Remez algorithm: {ang_seq}")

        PlotQSPResponse(ang_seq, target=poly, signal_operator="Wx")


if __name__ == '__main__':
    main()
