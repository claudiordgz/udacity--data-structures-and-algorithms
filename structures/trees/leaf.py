def Count_Binary_Tree_Leafs(node):
    """
    Find the number of leafs on a binary tree

    Args:
       tree(object): Input binary tree
    Returns:
       int: The number of leafs of the tree
    """

    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return Count_Binary_Tree_Leafs(node.left) + Count_Binary_Tree_Leafs(node.right)


class Tree:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)

f = Tree("F")
e = Tree("E", None, f)

d = Tree("D")
b = Tree("B", d, e)

c = Tree("C")
a = Tree("A", b, c)

my_tree = a

print ("Pass" if (3 == Count_Binary_Tree_Leafs(my_tree)) else "Fail")
