import latexify

from bees.formula_node import equ


def main():
    return {
        "_": "I have one subsection",
        "subsection": "Hello world" + equ(x_squared),
    }

@latexify.function
def x_squared(x):
    return x ** 2