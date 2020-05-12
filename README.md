# Arduino-Python 4-Axis Servo Control

Control four (or more) RC servos with Arduino and Python.

Please read the [associated blog post](https://bws428.github.io/notes/arduino-python-4-axis-servo/) for more details and a full description of the code.

https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e

## Installing `pipenv'

OKAY we're going to use `pipenv'

Python 3.5: The use of `venv` is now recommended for creating virtual environments. [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
python3 -m pip install --user --upgrade pip
```

```bash
python3 -m pip --version
```

## Installation

Clone this repo onto your local machine as follows:

```bash
git clone https://github.com/bws428/arduino-python-servos.git servos
```

Change into the project directory:

```bash
cd servos
```

## Create a Python 3 Virtual Environment

To ensure that all of the packages play nice with one another, we'll install a Python 3 virtual environment in a directory we'll name `venv`.

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

With the virtual environment activated, your shell prompt should now look something like this:

```bash
(venv) username@host:~/path/to/servos $
```

## Install the Required Packages

```bash
pip install requirements.txt
```

## Usage

TODO...

### References

- JT Paasch, [The Right Way to Use Virtual Environments](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7)
