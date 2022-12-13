# quantum-signal-proseccing
Quantum signal processing is built on interleaving 2 types of single-qubit rotations. A signal rotation operator and a signal processing operator. This repository includes classes that a demonstrate how these are combined into QSP control sequence which allow us to do signal processing on qubits.

# Usage
The script has two functions, `qsp_seq` and `qsp`. `qsp_sequence` evaluates the
QSP sequence as defined in the paper by Martyn et.al. and demonstrates how 
transitions probabilities can be modified using the signal rotation operator,
W and the signal processing operator S.

To see how the transition probabilities are affected by the rotation operator
provide a angle sequence \phi:

```
$ python main.py -qsp_seq (math.pi/2, 0.5*math.acos(-0.25), math.acos(-0.25), 0, -2*math.acos(-0.25), 0.5*math.acos(-0.25)) 
```
