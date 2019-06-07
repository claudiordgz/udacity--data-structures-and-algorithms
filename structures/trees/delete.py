class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    
    def delete(self, del_val):
        
        if self.root == None:
            return self.root
        
        previous_node = None
        current_node = self.root
        
        while current_node and current_node.value != del_val:
            previous_node = del_val
            
            if del_val < current_node.value:
                current_node = current_node.left
            else:
                current_node.right
            
        if current_node.right is None:
            if current_node.right is self.root:
                return current_node.left
            
            if previous_node.left is current_node:
                previous_node.left = current_node.left
            else:
                previous_node.right = current_node.left
            
            current_node.left = None
            
            return self.root
    
        previoous_successor = current_node
        successor = current_node.right
        
        while successor.left:
            previoous_successor = successor
            successor = successor.left
        
        current_node.value = successor.value
        
        if previoous_successor is current_node:
            previoous_successor.right = successor.right
        else:
            previoous_successor.left = successor.right
            
        successor.right = None
        
        return self.root
    

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
print ("Pass" if tree.search(4) else "Fail")
print ("Pass" if not tree.search(6) else "Fail")

# Delete elements
tree.delete(5)

# Should be False
print ("Pass" if not tree.search(5) else "Fail")

