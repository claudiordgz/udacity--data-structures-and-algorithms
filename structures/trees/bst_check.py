def check_BST(node, lower, upper):
    """
    Determine wether the input is a binary tree or not

    Args:
       tree(object): A BST object
    Returns:
       bool: True if it is a BST and False if not
    """
    if node is None:
        return True

    if node.value < lower or node.value > upper:
        return False

    return (check_BST(node.left, lower, node.value -1) and
          check_BST(node.right, node.value + 1, upper))

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

lower = 0
upper = 100

print ("Pass" if check_BST(my_tree, lower, upper) else "Fail")

