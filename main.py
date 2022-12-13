import sys
import math

from qsp_operation import Evaluate, PlotResponse

from angle_sequence import QuantumSignalProcessingPhases
from response import PlotQSPResponse 
from poly import StringPolynomial

def main():
    args = sys.argv[1:]
    cmd = args[0][1:]
    arg = args[1:]

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
        if(len(arg) == 2):
            poly = StringPolynomial(arg[0], arg[1])
        else:
            poly = StringPolynomial(arg[0], 10)
         
        ang_seq = QuantumSignalProcessingPhases(poly, method="tf")
        PlotQSPResponse(ang_seq, target=poly, signal_operator="Wx")

if __name__ == '__main__':
    main()
