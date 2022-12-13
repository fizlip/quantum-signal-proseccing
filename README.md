# quantum-signal-proseccing
Quantum signal processing is built on interleaving 2 types of single-qubit rotations. A signal rotation operator and a signal processing operator. This repository includes classes that a demonstrate how these are combined into QSP control sequence which allow us to do signal processing on qubits.

# Usage

The script has two functions, `qsp_seq` and `qsp`. `qsp_sequence` evaluates the
QSP sequence as defined in the paper by Martyn et.al. and demonstrates how 
transitions probabilities can be modified using the signal rotation operator,
W and the signal processing operator S.

## QSP Sequence
To evaluate the transition probabilities using the rotation operator and signal
operator you need to provide an phase angle sequence \phi:

```
$ main.py -qsp_seq 1,1,1,1
```
Here 1,1,1,1 is a simple angle sequence used as an example. This command 
plots the transition probabilities and compares it to the trivial case where
phi = (0,0) (i.e. no signal processing)


The BB1 filter has also been implemented and can be compared with the trivial
case:
```
$ main.py -qsp_seq bb1
```

## QSP

To calculate the phase angle sequence for a polynomial and plot the 
resulting approximation use:

```
$ main.py -qsp 'x**2'
```

Non-trivial functions (e.g. cos(x)) can also be approximated using numpy:

```
$ main.py -qsp 'np.cos(x**2)'
```

## Help
Use

```
$ main.py -help
```

to get additional documentation about the script.

# References
