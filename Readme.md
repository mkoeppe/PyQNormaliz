# PyQNormaliz - An interface to QNormaliz


## What is PyQQNormaliz

PyQQNormaliz provides an interface to QNormaliz (https://www.normaliz.uni-osnabrueck.de) via libQNormaliz.
It offers the complete functionality of QNormaliz, and can be used interactively from python. For a first example,
see [this introduction](examples/PyQNormaliz_Tutorial.ipynb) by Richard Sieg.

## Requirements

* python 2.7 or higher or python 3.4 or higher
* Recent version of QNormaliz (https://github.com/Normaliz/Normaliz/tree/enfnormaliz2018)

## Installation

You need to have QNormaliz installed on your system via the following commands
```
git clone https://github.com/Normaliz/Normaliz.git
cd Normaliz
git checkout enfnormaliz2018
NORMALIZ_PATH=${PWD}
./install_normaliz_with_qnormaliz_eantic.sh
make install
```
is enough. If you prefer or are not able to install it, you need to set CPATH and
LD_LIBRARY_PATH accordingly.

After that, you can install PyQNormaliz via
```
git clone https://github.com/sebasguts/PyQNormaliz.git
cd PyQNormaliz
python setup.py build_ext --include-dirs=${NORMALIZ_PATH}/nmz_opt_lib/include --library-dirs=${NORMALIZ_PATH}/nmz_opt_lib/lib
python setup.py install
```

## Usage

The main command is `NmzCone` to create a cone, and the member functions
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
PyQNormaliz_cpp.NmzCompute(C, "SupportHyperplanes")
```
or
```
PyQNormaliz_cpp.NmzCompute(C, ["SupportHyperplanes"])
```

NmzIsComputed takes a cone and a string representing an output property, and returns true if the
property is already computed for the cone, false otherwise.
```
PyQNormaliz_cpp.NmzIsComputed(C, "SupportHyperplanes")
```

NmzResult takes a cone and a string representing an output property, and returns the computed
value of this property as a matrix, a list, or as a bool.
```
PyQNormaliz_cpp.NmzResult(C, "SupportHyperplanes")
```