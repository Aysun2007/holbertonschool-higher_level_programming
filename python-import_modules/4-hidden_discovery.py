#!/usr/bin/python3
import sys
import types
import importlib.util
def discover_names_from_pyc(pyc_file):
    # Load the .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Retrieve all names in the module that do not start with '__'
    names = dir(module)
    filtered_names = [name for name in names if not name.startswith('__')]
    # Sort the names alphabetically and print each one on a new line
    filtered_names.sort()
    for name in filtered_names:
        print(name)
if __name__ == "__main__":
    pyc_file = '/tmp/hidden_4.pyc'
    discover_names_from_pyc(pyc_file)
