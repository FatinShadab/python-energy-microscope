import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from energy_module.decorator import measure_energy_to_csv
from time_modules.decorator import measure_time_to_csv
from input import __default__

import sys

class TreeNode:
    """
    A class representing a binary tree node. Each node can have a left and right child.

    Attributes:
        left: A TreeNode instance representing the left child.
        right: A TreeNode instance representing the right child.
    """
    def __init__(self, left: 'TreeNode' = None, right: 'TreeNode' = None) -> None:
        """
        Initializes a binary tree node with optional left and right children.

        Args:
            left (TreeNode, optional): The left child of the node. Defaults to None.
            right (TreeNode, optional): The right child of the node. Defaults to None.
        """
        self.left = left
        self.right = right

def make_tree(depth: int) -> TreeNode:
    """
    Creates a binary tree of the specified depth.

    This function recursively allocates nodes until the desired depth is reached.
    For a depth of 0, a leaf node is created.

    Args:
        depth (int): The depth of the binary tree.

    Returns:
        TreeNode: The root of the binary tree.
    """
    if depth > 0:
        return TreeNode(make_tree(depth - 1), make_tree(depth - 1))
    return TreeNode()

def check_tree(node: TreeNode) -> int:
    """
    Walks the binary tree to count the total number of nodes.

    This function recursively traverses the tree, summing the nodes at each step.

    Args:
        node (TreeNode): The root of the tree to be checked.

    Returns:
        int: The total number of nodes in the tree.
    """
    if node.left is None and node.right is None:
        return 1
    return 1 + check_tree(node.left) + check_tree(node.right)

def main(n: int) -> None:
    """
    Main function to run the binary tree algorithm. It allocates and deallocates trees
    of various depths, calculates the number of nodes, and outputs results.

    Args:
        n (int): The maximum depth for the trees to be allocated. If not provided,
                 the default value is 10.
    """
    min_depth = 4
    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1
    
    # Stretch tree: Allocates a tree of depth `stretch_depth` and counts its nodes.
    stretch_tree = make_tree(stretch_depth)
    print(f"stretch tree of depth {stretch_depth}\t check: {check_tree(stretch_tree)}")
    del stretch_tree
    
    # Long-lived tree: Allocates a tree of depth `max_depth` that persists while other trees are deallocated.
    long_lived_tree = make_tree(max_depth)
    
    # Allocate and walk binary trees of increasing depth
    for depth in range(min_depth, max_depth + 1, 2):
        iterations = 2 ** (max_depth - depth + min_depth)
        check = 0
        # Allocate and check multiple trees for each depth
        for _ in range(iterations):
            temp_tree = make_tree(depth)
            check += check_tree(temp_tree)
        print(f"{iterations}\t trees of depth {depth}\t check: {check}")
    
    # Output result for the long-lived tree
    print(f"long lived tree of depth {max_depth}\t check: {check_tree(long_lived_tree)}")

@measure_energy_to_csv(n=__default__["binary-trees"]["test_n"], csv_filename="binary_trees_pycompile")
def run_energy_benchmark(n: int) -> None:
    main(n)

@measure_time_to_csv(n=__default__["binary-trees"]["test_n"], csv_filename="binary_trees_pycompile")
def run_time_benchmark(n: int) -> None:
    main(n)


if __name__ == "__main__":
    n = __default__["binary-trees"]["depth"]
    
    run_energy_benchmark(n)
    run_time_benchmark(n)
