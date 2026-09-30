import os
import sys


def test_ruff(name, age):
    print(os.getcwd())
    return {"name": name, "age": age, "args": sys.argv}
