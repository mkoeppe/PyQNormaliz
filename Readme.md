# PyQNormaliz - An interface to QNormaliz


## What is PyQQNormaliz

PyQQNormaliz provides an interface to QNormaliz (https://www.normaliz.uni-osnabrueck.de) via libQNormaliz.
It offers the complete functionality of QNormaliz, and can be used interactively from python. For a first example,
see [this introduction](examples/PyQNormaliz_Tutorial.ipynb) by Richard Sieg.

## Requirements

* python 2.7 or higher or python 3.4 or higher
* QNormaliz 3.2.1 Oor higher (https://github.com/Normaliz/Normaliz/releases)

## Installation

You need to have QNormaliz properly installed and libQNormaliz in your gcc's include path.
On most systems, installing QNormaliz via
```
$ make install
```
is enough. If you prefer or are not able to install it, you need to set CPATH and
LD_LIBRARY_PATH accordingly.

After that, you can install PyQNormaliz via
```
$ pip install PyQNormaliz
```

## Usage

The main command is Cone to create a cone, and the member functions
of the cone class to compute properties. For a full list of input and output
properties, see the QNormaliz manual.

To create a cone, use
```
import PyQNormaliz_cpp
C = PyQNormaliz_cpp.NmzCone(number_field="min_poly (a2-2) embedding 1.4+/-0.1",cone=[[[1],[0,1]],[[1],[-1]]])
```

All possible QNormaliz input properties can be given as keyword arguments.

NmzCompute takes a cone as first argument, followed by arbitrary many strings, or a list of strings,
describing QNormaliz output properties. NmzCompute lets QNormaliz compute the necessary values, and
returns true if everything was computed properly, false otherwise.
```
NmzCompute(C, "SupportHyperplanes")
```
or
```
NmzCompute(C, ["SupportHyperplanes"])
```

NmzIsComputed takes a cone and a string representing an output property, and returns true if the
property is already computed for the cone, false otherwise.
```
NmzIsComputed(C, "SupportHyperplanes")
```

NmzResult takes a cone and a string representing an output property, and returns the computed
value of this property as a matrix, a list, or as a bool.
```
NmzResult(C, "SupportHyperplanes")
