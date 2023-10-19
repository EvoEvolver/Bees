import pytest
import types
from bees.node import *

def test_StringNode():
    node = StringNode("Hello world!")
    assert node.render() == "Hello world!"
    
def test_SectionNode():
    node = SectionNode({"section": "Hello world!"})
    assert node.render() == {"section": "Hello world!"}
    
def test_FunctionNode():
    node = FunctionNode(lambda: 3 ** 2)
    assert node.render() == 9
    
def test_ModuleNode1():
    bogus_module = types.ModuleType('bogus_module')
    bogus_module.main = lambda: "Hello world!"
    node = ModuleNode(bogus_module)
    assert node.render() == "Hello world!"
    
def test_ModuleNode2():
    bogus_module = types.ModuleType('bogus_module')
    bogus_module.not_main = lambda: "Hello world!"
    with pytest.raises(ValueError):
        ModuleNode(bogus_module)
