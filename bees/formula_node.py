import latexify

from bees.node import Node


class FormulaNode(Node):
    def __init__(self, formula_function):
        super().__init__()
        self.formula_function = formula_function
        self.decomposed = False

    def render(self):
        raise NotImplementedError

    def __repr__(self):
        return f"FormulaNode({self.formula_function})"


def equ(formula_function):
    return FormulaNode(formula_function)