import py_compile
from sys import argv
if len(argv)<2:
    print("usage: python compile.py dest.py")
else:
    py_compile.compile(argv[1])
