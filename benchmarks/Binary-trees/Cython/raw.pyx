from libc.stdlib cimport malloc, free

cdef struct TreeNode:
    # C structure representing a binary tree node.
    # Each node contains pointers to left and right children.
    TreeNode* left  # Pointer to left child
    TreeNode* right  # Pointer to right child

cdef TreeNode* make_tree(int depth):
    # Recursively creates a binary tree of the specified depth.
    
    # Allocate memory for a new node
    cdef TreeNode* node = <TreeNode*>malloc(sizeof(TreeNode))
    
    # Check if memory allocation failed
    if not node:
        raise MemoryError("Failed to allocate memory for TreeNode")
    
    # Initialize child pointers to NULL
    node.left = NULL
    node.right = NULL
    
    # Recursively create left and right children if depth > 0
    if depth > 0:
        node.left = make_tree(depth - 1)
        node.right = make_tree(depth - 1)
    
    return node

# Define check_tree to work directly with C pointers.
cdef int check_tree(TreeNode* node):
    # Counts the total number of nodes in the binary tree.
    # Args:
    #    node (TreeNode*): Pointer to the root of the tree.
    # Returns:
    #   int: The total number of nodes in the tree.

    if node == NULL:
        return 0  # Return 0 if the node is NULL to avoid segmentation faults
    
    # Directly access node's left and right pointers (as C objects)
    return 1 + check_tree(node.left) + check_tree(node.right)

def main(int n):
    # Main function to execute the binary tree operations.
    # Allocates and deallocates trees of various depths,
    # calculates the number of nodes, and outputs results.
    # Args:
    #    n (int): The maximum depth for the trees to be allocated.

    cdef int min_depth = 4
    cdef int max_depth = max(min_depth + 2, n)
    cdef int stretch_depth = max_depth + 1
    cdef TreeNode* stretch_tree
    
    # Stretch tree: Creates a tree of depth `stretch_depth` and counts its nodes.
    stretch_tree = make_tree(stretch_depth)
    print(f"stretch tree of depth {stretch_depth}\t check: {check_tree(stretch_tree)}")
    free(stretch_tree)
    
    # Long-lived tree: Allocates a tree of depth `max_depth` that persists while other trees are deallocated.
    cdef TreeNode* long_lived_tree = make_tree(max_depth)
    
    # Iterate over depths, creating and checking multiple trees per depth.
    cdef int depth, iterations, check, i
    cdef TreeNode* temp_tree
    
    for depth in range(min_depth, max_depth + 1, 2):
        iterations = <int>(2 ** (max_depth - depth + min_depth))  # Ensure `iterations` is an integer
        check = 0
        
        for i in range(iterations):
            temp_tree = make_tree(depth)
            check += check_tree(temp_tree)
            free(temp_tree)
        
        print(f"{iterations}\t trees of depth {depth}\t check: {check}")
    
    # Output result for the long-lived tree.
    print(f"long lived tree of depth {max_depth}\t check: {check_tree(long_lived_tree)}")
    free(long_lived_tree)
