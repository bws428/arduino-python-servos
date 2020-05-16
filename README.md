# Arduino-Python Servos

Control four (or more) RC servos with Arduino and Python.

Please read the [associated blog post](https://bws428.github.io/notes/arduino-python-4-axis-servo/) for more details and a full description of the code.

## Installing `pipenv` for managing dependencies

OKAY we're going to use [pipenv](https://pipenv.pypa.io/en/latest/)

```bash
python3 -m pip install --user --upgrade pip
```

```bash
python3 -m pip --version
```

```bash
python3 -m pip install --user pipenv
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

Install the project's dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

With the virtual environment activated, your shell prompt should now look something like this:

```bash
(servos) username@host:~/path/to/servos $
```

## Usage

TODO...

### References

- JT Paasch, [The Right Way to Use Virtual Environments](https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7)

- https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e
