def print_tree_postorder(tree):
    """
    Implement a post-order traversal here

    Args:
       tree(object): A binary tree input
    Returns:
       None
    """
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree, end=' ')

print("Post-order:", end=' ')
print_tree_postorder(my_tree)
