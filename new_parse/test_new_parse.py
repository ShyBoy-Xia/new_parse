import os, sys
import pytest
from new_parse import new_parse


def test_parse():
    rootName = "data/root.pkl"
    dictName = 'data/dict.txt'
    fileName = 'data/xi.txt'
    N = 100
    assert new_parse(rootName, dictName, fileName, N)
