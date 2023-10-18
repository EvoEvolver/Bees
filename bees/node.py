from typing import Callable


class Node:

    def __init__(self):
        self._content = None
        self.children = []

    def render(self):
        raise NotImplementedError

    def __add__(self, other):
        return JointNode([self, other])

    def __radd__(self, other):
        if isinstance(other, str):
            self.children.append(other)
            return self
        else:
            raise NotImplementedError


class JointNode(Node):
    def __init__(self, nodes):
        super().__init__()
        self.children = nodes

    def render(self):
        return self.children

    def __add__(self, other):
        if isinstance(other, JointNode):
            self.children.extend(other.children)
            return self
        else:
            self.children.append(node(other))
            return self

    def __radd__(self, other):
        if isinstance(other, str):
            self.children.insert(0, other)
            return self
        else:
            raise NotImplementedError


class StringNode(Node):
    def __init__(self, string):
        super().__init__()
        self._content: str = string
        self.children = None

    def render(self):
        return self._content


class SectionNode(Node):
    def __init__(self, content_dict: dict):
        super().__init__()
        self._content: str = content_dict.get("_", "")
        self.children = [(title, content) for title, content in content_dict.items() if
                         title != "_"]


class FunctionNode(Node):
    def __init__(self, func: Callable):
        super().__init__()
        self._content: Callable = func

    def render(self):
        res = self._content()
        if isinstance(res, dict):
            return SectionNode(res)
        else:
            return res


def node(src=None):
    if src is None:
        return JointNode([])
    if isinstance(src, str):
        return StringNode(src)
    if isinstance(src, dict):
        return SectionNode(src)
    if isinstance(src, list):
        return JointNode([node(s) for s in src])
    if isinstance(src, Node):
        return src
    if isinstance(src, Callable):
        return FunctionNode(src)
    raise NotImplementedError
