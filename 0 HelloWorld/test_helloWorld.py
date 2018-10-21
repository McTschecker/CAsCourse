### Copyright Fabian Blank
import pytest
from helloworld import hello

def test_HelloWorld(capsys):
    hello()
    printed = capsys.readouterr()
    assert printed.out == "Hello World!\n"
