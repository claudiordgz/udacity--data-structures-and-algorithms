def print_tree_preorder(tree):
    """
    Implement a pre-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if tree == None: return
    print(tree, end=' ')
    print_tree_preorder(tree.left)
    print_tree_preorder(tree.right)

print("Pre-order:", end=' ')
print_tree_preorder(my_tree)
