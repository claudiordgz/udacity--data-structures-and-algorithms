

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def _print(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __repr__(self):
        return self._print()

    def __str__(self):
        return self._print()

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.num_elements += 1
            return

        node = self.tail
        node.next = Node(value)
        self.tail = node.next
        self.num_elements += 1

    def size(self):
        return self.num_elements


def list_generator(llist):
    itr = llist.head
    while itr:
        yield itr.value
        itr = itr.next


def union(llist_1, llist_2):
    l1 = list_generator(llist_1)
    l2 = list_generator(llist_2)
    un = dict()
    for i in l1:
        un[i] = 0

    for i in l2:
        un[i] = 0

    r = LinkedList()
    for i in un.keys():
        r.append(i)

    return r


def intersection(llist_1, llist_2):
    keys1 = {i: 0 for i in list_generator(llist_1)}
    keys2 = {i: 0 for i in list_generator(llist_2)}

    r = LinkedList()
    for i in keys1.keys():
        if i in keys2:
            r.append(i)

    return r


def validate_lists(llist_1, llist_2):
    print("EXPECTED:", llist_1)
    print("RESULT:", llist_2)
    if llist_1.size() != llist_2.size():
        return False

    itr1 = llist_1.head
    itr2 = llist_2.head
    while itr1 is not None or itr2 is not None:
        if itr1 is None and itr2 is not None:
            return False
        if itr2 is None and itr1 is not None:
            return False
        if itr1.value != itr2.value:
            return False
        itr1 = itr1.next
        itr2 = itr2.next
    return True


def base_test_case(ll1, ll2, expected_union, expected_intersection):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    expected_intersection_list = LinkedList()
    expected_union_list = LinkedList()

    for i in ll1:
        linked_list_1.append(i)

    for i in ll2:
        linked_list_2.append(i)

    for i in expected_union:
        expected_union_list.append(i)

    for i in expected_intersection:
        expected_intersection_list.append(i)

    un = union(linked_list_1, linked_list_2)
    print("TEST UNION:", validate_lists(expected_union_list, un))
    inters = intersection(linked_list_1, linked_list_2)
    print("TEST INTERSECTION:", validate_lists(expected_intersection_list, inters))


# Test case 1
def test_case_1():
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    expected_union = [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
    expected_intersection = [4, 6, 21]

    base_test_case(element_1, element_2, expected_union, expected_intersection)
    # EXPECTED: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    # RESULT: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
    # TEST UNION: True
    # EXPECTED: 4 -> 6 -> 21 ->
    # RESULT: 4 -> 6 -> 21 ->
    # TEST INTERSECTION: True


# Test case 2
def test_case_2():
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]
    expected_union = [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
    expected_intersection = []

    base_test_case(element_1, element_2, expected_union, expected_intersection)
    # EXPECTED: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    # RESULT: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
    # TEST UNION: True
    # EXPECTED:
    # RESULT:
    # TEST INTERSECTION: True


def test_case_3():
    element_1 = []
    element_2 = []
    expected_union = []
    expected_intersection = []

    base_test_case(element_1, element_2, expected_union, expected_intersection)
    # EXPECTED:
    # RESULT:
    # TEST UNION: True
    # EXPECTED:
    # RESULT:
    # TEST INTERSECTION: True


test_case_1()
test_case_2()
test_case_3()
