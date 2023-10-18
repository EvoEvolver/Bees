import latexify

from bees.node import Node


class FormulaNode(Node):
    def __init__(self, formula_function):
        super().__init__()
        self.formula_function = formula_function

    def render(self):
        return str(self.formula_function)


def equ(formula_function):
    return FormulaNode(formula_function)