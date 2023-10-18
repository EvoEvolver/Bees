from bees.node import node
from bees.render import render_to_tree


def a():
    return "This is a paragraph"


def main():
    return {
        "_": "This is the content outside of sections",
        "introduction": "This is an introduction",
        "the first section": node(a) + "123",
        "the section section": node() + a + "456",
        "conclusion": "This is a conclusion",
    }


res = render_to_tree(main())

print(res)
