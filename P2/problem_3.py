
from collections import deque


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list

    midpoint = len(input_list) // 2
    left = input_list[:midpoint]
    right = input_list[midpoint:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def str_list_to_int(l):
    return int("".join(l))


def rearrange_digits(input_list, sort_fn):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    l = sort_fn(input_list)
    _the_list = input_list if l is None else l
    n = len(input_list)
    i, j = (n // 2, n // 2) if n % 2 == 0 else ((n // 2) + 1, n // 2)
    results = [[], []]
    for el in _the_list:
        if i >= j:
            results[0].append(str(el))
            i -= 1
        else:
            results[1].append(str(el))
            j -= 1
    return (str_list_to_int(results[0]), str_list_to_int(results[1]))


"""
The following code was to test a heapsort implementation.
It worked, but I preferred the merge sort one because it is
less code.
"""


def to_comma_sep_str(l):
    return ",".join(map(str, l))


def test_heapify(input_list, expected):
    a = "from: [{}] => to: ".format(to_comma_sep_str(input_list))
    heapify(input_list)
    a = "{}[{}]".format(a, to_comma_sep_str(input_list))
    print(input_list == expected, a)


class Queue:

    def __init__(self):
        self.arr = deque()

    def push(self, el):
        self.arr.appendleft(el)

    def pop(self):
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.size() == 0


def get_max_index(input_list, right_index, left_index, top_index=None):
    top = len(input_list) if top_index is None else top_index
    right_index = None if right_index >= top else right_index
    left_index = None if left_index >= top else left_index

    if right_index is None and left_index is None:
        return None

    if right_index is None:
        return left_index

    max_index = right_index if input_list[right_index] > input_list[left_index] else left_index
    return max_index


def down_heapify(input_list, parent_idx, top_index=None):
    q = Queue()
    q.push(parent_idx)

    while not q.is_empty():
        parent_index = q.pop()
        if top_index is not None and parent_index >= top_index:
            return

        left_index = (parent_index * 2) + 1
        right_index = (parent_index * 2) + 2

        max_index = get_max_index(
            input_list, right_index, left_index, top_index)
        if max_index is None:
            continue  # None is possible when traversing down

        if input_list[max_index] > input_list[parent_index]:
            input_list[max_index], input_list[parent_index] = input_list[parent_index], input_list[max_index]
            q.push(max_index)


def heapify(input_list):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    i = len(input_list) // 2

    while i > 0:

        right_index = i * 2
        left_index = (i * 2) - 1
        parent_index = (right_index - 1) // 2

        max_index = get_max_index(input_list, right_index, left_index)
        if max_index is None:
            raise IndexError("A child is expected here")

        if input_list[max_index] > input_list[parent_index]:
            input_list[max_index], input_list[parent_index] = input_list[parent_index], input_list[max_index]
            down_heapify(input_list, max_index)

        i -= 1

    return input_list


def heapsort(input_list):
    heapify(input_list)
    i = len(input_list) - 1
    while i >= 0:
        input_list[0], input_list[i] = input_list[i], input_list[0]
        down_heapify(input_list, 0, i)
        i -= 1
    input_list.reverse()


test_heapify([1, 16, 5, 30, 27, 17, 20, 2, 60, 3, 95],
             [95, 60, 20, 30, 27, 17, 5, 2, 1, 3, 16])
# True from: [1,16,5,30,27,17,20,2,60,3,95] => to:
# [95,60,20,30,27,17,5,2,1,3,16]
test_heapify([0, 1, 2], [2, 1, 0])
# True from: [0,1,2] => to: [2,1,0]
test_heapify([], [])
# True from: [] => to: []
test_heapify([4, 6, 2, 5, 9, 8], [9, 6, 8, 5, 4, 2])
# True from: [4,6,2,5,9,8] => to: [9,6,8,5,4,2]
test_heapify([1, 2, 3, 4, 5], [5, 4, 3, 1, 2])
# True from: [1,2,3,4,5] => to: [5,4,3,1,2]


def test_heapsort(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [9, 9, 8, 7, 6, 5, 4, 4, 3, 3, 1, 0]
test_case = [arr, solution]
test_heapsort(test_case)
# Pass

arr = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
solution = [5, 5, 5, 4, 4, 4, 4, 3, 3, 3]
test_case = [arr, solution]
test_heapsort(test_case)
# Pass

arr = [99]
solution = [99]
test_case = [arr, solution]
test_heapsort(test_case)
# Pass

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [21, 12, 5, 2, 1, 0, 0]
test_case = [arr, solution]
test_heapsort(test_case)
# Pass


def base_test_function(test_case, sort_fn):
    output = rearrange_digits(test_case[0], sort_fn)
    solution = test_case[1]
    a = "output: {}, solution: {}".format(output, solution)
    if sum(output) == sum(solution):
        print("Pass", a)
    else:
        print("Fail", a)


def test_function_mergesort(test_case):
    base_test_function(test_case, mergesort)


test_function_mergesort([[1, 2, 3, 4, 5], [542, 31]])
# Pass output: (542, 31), solution: [542, 31]
test_function_mergesort([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass output: (964, 852), solution: [964, 852]
test_function_mergesort([[0, 1], [1, 0]])
# Pass output: (1, 0), solution: [1, 0]
test_function_mergesort([[0, 1, 2], [21, 0]])
# Pass output: (21, 0), solution: [21, 0]


def test_function_heapsort(test_case):
    base_test_function(test_case, heapsort)


test_function_heapsort([[1, 2, 3, 4, 5], [542, 31]])
# Pass output: (542, 31), solution: [542, 31]
test_function_heapsort([[4, 6, 2, 5, 9, 8], [964, 852]])
# Pass output: (964, 852), solution: [964, 852]
test_function_heapsort([[0, 1], [1, 0]])
# Pass output: (1, 0), solution: [1, 0]
test_function_heapsort([[0, 1, 2], [21, 0]])
# Pass output: (21, 0), solution: [21, 0]
