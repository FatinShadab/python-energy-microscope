import ctypes
from ctypes import c_int, c_char_p

# Load the shared library
lib = ctypes.CDLL("./libhanoi.so")

# Declare the argument types for the C function
lib.towers_of_hanoi.argtypes = [c_int, c_char_p, c_char_p, c_char_p]
lib.towers_of_hanoi.restype = None

# Call the C function from Python
def run_hanoi(n):
    source = b"A"      # b"A" = byte string
    auxiliary = b"B"
    target = b"C"

    lib.towers_of_hanoi(n, source, auxiliary, target)


if __name__ == "__main__":
    try:
        run_hanoi(3)
    except Exception as e:
        print(f"Error: {e}")
