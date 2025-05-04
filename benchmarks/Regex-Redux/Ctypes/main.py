import ctypes
import os

# Load the shared library
lib = ctypes.CDLL("./libregexredux.so")  # Or "regexredux.dll" on Windows

# Define argument types for the function
lib.regex_redux.argtypes = [ctypes.c_char_p]
lib.regex_redux.restype = None

def run_regex_redux(file_path: str):
    print("Running Regex Redux from C:")
    lib.regex_redux(file_path.encode('utf-8'))

if __name__ == "__main__":
    run_regex_redux("input_fasta.txt")
