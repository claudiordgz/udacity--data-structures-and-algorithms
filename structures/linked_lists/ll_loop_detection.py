# Solution

def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    if linked_list.head is None:
        return False
    
    slow = linked_list.head
    fast = linked_list.head
    
    while fast and fast.next:
        # if a node refers to itself, that's a little loop
        if slow.next == slow:
            return True
        
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two nodes
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
    # the list has an end and isn't circular
    return False

print ("Pass" if (iscircular(list_with_loop) == True) else "Fail")
print ("Pass" if  (iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print ("Pass" if  (iscircular(LinkedList([1])) == False) else "Fail")
