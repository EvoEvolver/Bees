from typing import Dict, Tuple, Any, Callable, List

from bees.node import Node, FunctionNode, ModuleNode
from types import ModuleType


def render_to_tree(src) -> Dict:
    if src is None:
        return {}
    if isinstance(src, str):
        return {"_": src}
    while True:
        res, finished = render_to_node(src)
        if finished:
            return res
        else:
            src = res


def render_to_node(src) -> Tuple[Any, bool]:
    if src is None:
        return "", True
    if isinstance(src, str):
        return src, True
    if isinstance(src, dict):
        return render_dict_to_tree(src)
    if isinstance(src, list):
        return render_list_to_tree(src)
    if isinstance(src, Node):
        if src.decomposed:
            return src.render(), False
        else:
            return src, True
    if isinstance(src, Callable):
        return FunctionNode(src).render(), False
    if isinstance(src, ModuleType):
        return ModuleNode(src).render(), False


def render_dict_to_tree(src: Dict) -> Tuple[Dict, bool]:
    tree_rendered = {}
    all_finished = True
    for key, value in src.items():
        if isinstance(value, str):
            tree_rendered[key] = value
        else:
            rendered, finished = render_to_node(value)
            tree_rendered[key] = rendered
            all_finished = all_finished and finished
    return tree_rendered, all_finished


def render_list_to_tree(src: List) -> Tuple[List | str, bool]:
    list_rendered = []
    strings = []
    all_finished = True
    for item in src:
        if isinstance(item, str):
            strings.append(item)
            continue
        else:
            list_rendered.append(" ".join(strings))
            strings = []
        list_rendered.append(item.render())
        all_finished = False
    list_rendered.append(" ".join(strings))
    if len(list_rendered) == 1:
        res = list_rendered[0]
        if isinstance(res, str):
            return res.strip(), True
        else:
            return res, True
    return list_rendered, all_finished
