import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import ctypes

# Load the shared library
if os.name == "nt":
    lib = ctypes.CDLL("binary_tree.dll")
else:
    lib = ctypes.CDLL("./libbinary_tree.so")

# Define TreeNode struct (forward declaration)
class TreeNode(ctypes.Structure):
    pass

TreeNodePtr = ctypes.POINTER(TreeNode)

TreeNode._fields_ = [("left", TreeNodePtr),
                     ("right", TreeNodePtr)]

# Set argument and return types
lib.make_tree.argtypes = [ctypes.c_int]
lib.make_tree.restype = TreeNodePtr

lib.check_tree.argtypes = [TreeNodePtr]
lib.check_tree.restype = ctypes.c_int

lib.free_tree.argtypes = [TreeNodePtr]
lib.free_tree.restype = None

def run_binary_trees(n: int):
    min_depth = 4
    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1

    # Stretch tree
    stretch_tree = lib.make_tree(stretch_depth)
    print(f"stretch tree of depth {stretch_depth}\t check: {lib.check_tree(stretch_tree)}")
    lib.free_tree(stretch_tree)

    # Long-lived tree
    long_lived_tree = lib.make_tree(max_depth)

    for depth in range(min_depth, max_depth + 1, 2):
        iterations = 2 ** (max_depth - depth + min_depth)
        check = 0
        for _ in range(iterations):
            temp_tree = lib.make_tree(depth)
            check += lib.check_tree(temp_tree)
            lib.free_tree(temp_tree)
        print(f"{iterations}\t trees of depth {depth}\t check: {check}")

    print(f"long lived tree of depth {max_depth}\t check: {lib.check_tree(long_lived_tree)}")
    lib.free_tree(long_lived_tree)

@measure_energy_to_csv(n=__default__["binary-trees"]["test_n"], csv_filename="binary_trees_ctypes")
def run_energy_benchmark(n: int) -> None:
    run_binary_trees(n)

@measure_time_to_csv(n=__default__["binary-trees"]["test_n"], csv_filename="binary_trees_ctypes")
def run_time_benchmark(n: int) -> None:
    run_binary_trees(n)


if __name__ == "__main__":
    n = __default__["binary-trees"]["depth"]
    
    run_energy_benchmark(n)
    run_time_benchmark(n)
