#include <stdlib.h>

typedef struct TreeNode {
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Create a tree of specified depth
TreeNode* make_tree(int depth) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    if (depth > 0) {
        node->left = make_tree(depth - 1);
        node->right = make_tree(depth - 1);
    } else {
        node->left = NULL;
        node->right = NULL;
    }
    return node;
}

// Recursively count nodes in the tree
int check_tree(TreeNode* node) {
    if (node->left == NULL && node->right == NULL) {
        return 1;
    }
    return 1 + check_tree(node->left) + check_tree(node->right);
}

// Free memory
void free_tree(TreeNode* node) {
    if (node == NULL) return;
    free_tree(node->left);
    free_tree(node->right);
    free(node);
}

// gcc -shared -o libbinary_tree.so -fPIC binary_tree.c