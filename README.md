# Quantum Signal Processing
Quantum signal processing is built on interleaving 2 types of single-qubit rotations. A signal rotation operator and a signal processing operator. This repository includes classes that a demonstrate how these are combined into QSP control sequence which allow us to do signal processing on qubits.

# Dependencies 
The main script uses TensorFlow to approximate values. 
To run the script you need to have this installed, all 
the dependencies are listed in in `requirements.txt` and
can be installed using 
```
pip install -r requirements.txt
```
The packages can be quite large so some demonstrations
of the script have also been saved in the `examples/`
folder so that you get an idea about the results without
having to run the program!

# Usage

The script has two functions, `qsp_seq` and `qsp`. `qsp_sequence` evaluates the
QSP sequence as defined in the paper by Martyn et.al. and demonstrates how 
transitions probabilities can be modified using the signal rotation operator,
**W** and the signal processing operator **S**.

`qsp` is the reverse of `qsp_seq`, given a polynomial it will approximate the 
phase angle sequence that constructs the polynomial. This involves 
quite heavy math. Initially a [*remez type*](https://en.wikipedia.org/wiki/Remez_algorithm) exchange algorithm was used for this.
This algorithm gives adequate results only for simple polynomial (x^2, x + 1 etc.).
The [`pyqsp`](https://github.com/ichuang/pyqsp) package made by Chuang et.al uses a `TensorFlow` model to approximate
these with much better accuracy. Their model is used in this package as well.

## QSP Sequence
To evaluate the transition probabilities using the rotation operator and signal
operator you need to provide a phase angle sequence \phi:

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

### Using Remez type exchange algorithm
An alternative and much faster approach than the one above is to use a 
Remez type exchange algorithm to approximate the angle sequence. This can be
computed using
```
$ main.py -qsp_remez 'x'
```
It is however much inferior in accuracy to the TensorFlow implementation.
Polynomials *n > 3* are not well approximated.

## Help
Use

```
$ main.py -help
```

to get additional documentation about the script.

# References
This repository implements ideas put forth by [this paper](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.040203) and [Chao et al.](https://github.com/alibaba-edu/angle-sequence). It also uses part of the accompanying [code base](https://github.com/ichuang/pyqsp).

It was made as part of the course 'Seminar: Advanced Topics of Quantum Computing (IN2107,IN2183,IN0014)' at TUM.
