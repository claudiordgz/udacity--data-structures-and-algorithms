import sys


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    pivot_index = binary_search_of_pivot(input_list)
    return binary_search(input_list, number, pivot_index)

def binary_search_of_pivot(input_list):
    if len(input_list) == 1:
        return 0

    start = 0
    end = len(input_list) - 1
    first_el = input_list[0]
    last_min = sys.maxsize
    last_min_index = -1

    while start <= end:
        midpoint = (start + end) // 2
        el = input_list[midpoint]
        if el >= first_el:
            # go right
            start = midpoint + 1
        else:
            # go left
            if el < last_min:
                last_min = el
                last_min_index = midpoint
            end = midpoint - 1
    return last_min_index

def binary_search(input_list, number, pivot_index):
    
    start = 0
    end = len(input_list) - 1

    while start <= end:
        midpoint = (start + end) // 2
        adjusted_midpoint = (pivot_index + midpoint) % len(input_list)
        if input_list[adjusted_midpoint] == number:
            return adjusted_midpoint
        elif input_list[adjusted_midpoint] > number:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    a = rotated_array_search(input_list, number)
    if linear_search(input_list, number) == a:
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass

def test_pivot_function(test_list, expected_pivot_value):
    pivot_index = binary_search_of_pivot(test_list)
    if test_list[pivot_index] == expected_pivot_value:
        print("Pass")
    else:
        print("Fail")

test_pivot_function([4,5,6,7,0,1,2], 0)
# Pass
test_pivot_function([9,10,25,35,90,125,0,3,6,7,8], 0)
# Pass
test_pivot_function([1,0], 0)
# Pass
test_pivot_function([0], 0)

t = list(range(0, 9999))
t = t[330:] + t[:330]
test_pivot_function(t, 0)
# Pass

t = list(range(345, 9999))
t = t[675:] + t[:675]
test_pivot_function(t, 345)
# Pass
