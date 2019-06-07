def lowest_common_ancestor(node, node_a, node_b):
    """
    Determine the lowest common ancestor

    Args:
       tree(object): A BST object
    Returns:
       int: Lowest shared ancestor
    """

    if node_a < node.value > node_b:
        return lowest_common_ancestor(node.left, node_a, node_b)

    if node_a > node.value < node_b:
        return lowest_common_ancestor(node.right, node_a, node_b)

    return node.value


class Tree:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)

f = Tree(4)
e = Tree(3, None, f)

d = Tree(1)
b = Tree(2, d, e)

c = Tree(6)
a = Tree(5, b, c)

my_tree = a

print ("Pass" if 2 == lowest_common_ancestor(my_tree, 1, 4) else "Fail")

