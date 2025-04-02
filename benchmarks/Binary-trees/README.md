
# Binary Trees
The Binary Trees Benchmarking Algorithm is designed to test the efficiency of memory allocation and garbage collection in programming languages by creating and manipulating binary trees of various depths. The program creates binary trees, walks through them to count the nodes, and deallocates the trees while measuring their memory usage.

This algorithm is part of the Computer Language Benchmarks Game (CLBG), which aims to compare the performance and memory management of different programming languages. In this case, the algorithm specifically focuses on the creation, traversal, and destruction of binary trees, offering insights into how efficiently a language handles memory management for recursive data structures.

## Algorithm

The algorithm works as follows:
1. **Tree Node Class**: Each node in the binary tree has two child nodes (left and right). A leaf node does not have children.
2. **Tree Creation**: The program recursively creates binary trees of varying depths. For each tree, the algorithm counts the nodes by recursively walking through it.
3. **Stretch Tree**: The program creates a stretch tree (a tree with depth `max_depth + 1`), counts its nodes, and then deletes it. This helps to test memory allocation and deallocation.
4. **Multiple Trees**: Trees of depths ranging from `min_depth` to `max_depth` are created and checked in multiple iterations. This helps to simulate the real-world scenario where many objects are allocated and deallocated.
5. **Long-Lived Tree**: A long-lived binary tree is created with the maximum depth and remains throughout the execution of the program to ensure that memory is not prematurely freed.

The program outputs the total number of nodes for each tree created, and the result is used to verify the correctness of the implementation while benchmarking memory efficiency.

## Pseudo Code

```plaintext
1. Define a TreeNode class with left and right children.
2. Define a function make_tree(depth):
   - If depth > 0:
     - Create a left child with depth-1.
     - Create a right child with depth-1.
     - Return a new node with the left and right children.
   - If depth = 0, return a leaf node (node with no children).
3. Define a function check_tree(node):
   - If the node is a leaf (no left or right children), return 1.
   - Recursively traverse left and right children, adding 1 for the current node.
4. In the main function:
   - Create a stretch tree with depth max_depth + 1 and check it.
   - Create a long-lived tree with depth max_depth and keep it throughout the program.
   - Iterate through tree depths from min_depth to max_depth, creating multiple trees at each depth, checking them, and deleting them.
   - For each iteration, print the number of trees created and the total number of nodes checked.
```

## Implementation Approach

The implementation involves the following steps:

1. **Tree Node Class**: A class `TreeNode` is defined to represent a node in the binary tree. Each node has two attributes `left` and `right`, which refer to the left and right children of the node. If both are `None`, the node is a leaf node.
   
2. **Tree Creation (`make_tree`)**: The `make_tree` function is a recursive function that creates a binary tree of the given depth. For any depth greater than 0, the function creates two child nodes, each of which calls `make_tree` recursively with `depth-1`. When the depth reaches 0, a leaf node is returned.

3. **Tree Traversal (`check_tree`)**: The `check_tree` function recursively counts the number of nodes in the tree. If a node is a leaf node (both `left` and `right` are `None`), it returns 1. Otherwise, it recursively counts the nodes in the left and right subtrees and returns the total number of nodes.

4. **Memory Allocation and Deallocation**: The program creates and deallocates trees in several stages:
   - A **stretch tree** is created with depth `max_depth + 1`, its nodes are counted, and it is then deleted.
   - A **long-lived tree** with depth `max_depth` is created and kept alive throughout the program.
   - Multiple trees of varying depths are created, walked, and deallocated, with the results printed at each stage.

5. **Benchmarking**: The program runs the algorithm for a range of tree depths and measures the number of nodes in each tree, simulating memory management through the creation and deallocation of binary trees.

## Time Complexity

The time complexity of the `check_tree` function is **O(n)**, where `n` is the number of nodes in the tree. Since every node in the tree must be visited once during the traversal, the complexity is linear with respect to the size of the tree.

The time complexity of the tree creation (`make_tree`) is **O(2^d)**, where `d` is the depth of the tree. This is because at each depth level, the function creates two child nodes, and the number of nodes doubles at each level.

Thus, the overall time complexity of the program is a combination of tree creation and traversal for multiple tree depths. The total time complexity can be considered as **O(2^d)** for each depth level, where `d` is the depth of the binary trees created.

## Space Complexity

The space complexity is primarily driven by the number of nodes created and the depth of recursion used for both tree creation and tree traversal.

- **Tree Nodes**: At each depth `d`, the number of nodes created is proportional to `2^d`. Hence, for the maximum depth `max_depth`, the space required for storing the binary trees is proportional to the total number of nodes created, which is **O(2^max_depth)**.
- **Recursive Stack**: The depth of the recursion stack is proportional to the maximum depth of the tree. Therefore, the space complexity for the recursive function calls is **O(max_depth)**.

Overall, the space complexity is **O(2^max_depth)** due to the number of nodes created in the binary tree.

## References Used for Implementation and Information

1. **Binary Trees Benchmark (CLBG)** - Computer Language Benchmarks Game:
   - https://benchmarksgame-team.pages.debian.net/benchmarksgame/
   
2. **Jeremy Zerfas' C Program for Binary Trees**:
   - This algorithm is inspired by Jeremy Zerfas's C program for binary trees in the Benchmarks Game.

3. **Eamon Nerbonne and Brad Chamberlain's Contributions**:
   - Their work in refining the algorithm for correctness and benchmarking memory management.

4. **Python Documentation**:
   - Official Python documentation for understanding memory management, recursion, and object handling.
   - https://docs.python.org/3/