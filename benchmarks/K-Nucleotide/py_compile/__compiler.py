import py_compile
import os

# Compile main.py to optimized bytecode
source_file = 'main.py'
compiled_file = py_compile.compile(source_file, cfile=None, dfile=None, doraise=True, optimize=2)

print(f"Optimized .pyc file created at: {compiled_file}")
