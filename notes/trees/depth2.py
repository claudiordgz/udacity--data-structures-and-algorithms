def print_tree_inorder(tree):
    """
    Implement a in-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if tree == None: return
    print_tree_inorder(tree.left)
    print(tree, end=' ')
    print_tree_inorder(tree.right)

print("In-order:", end=' ')
print_tree_inorder(my_tree)
