import ctypes
import time
import os
import sys

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


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    start = time.time()
    run_binary_trees(n)
    end = time.time()
    print(f"Execution time for n={n}: {end - start:.6f} seconds")
