def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zeros_idx = 0
    two_idx = len(input_list) - 1
    idx = 0

    while idx <= two_idx:
        el = input_list[idx]
        if el == 0:
            input_list[zeros_idx], input_list[idx] = input_list[idx], input_list[zeros_idx]
            zeros_idx += 1
            idx += 1
        elif el == 2:
            input_list[two_idx], input_list[idx] = input_list[idx], input_list[two_idx]
            two_idx -= 1
        else:
            idx += 1
    return input_list


def test_function(test_case):
    sorted_array = [i for i in test_case]
    a = "[{}]".format(",".join(map(str, sorted_array)))
    sort_012(sorted_array)
    a = "{} => {}".format(a, "[{}]".format(",".join(map(str, sorted_array))))
    if sorted_array == sorted(test_case):
        print("Pass", a)
    else:
        print("Fail", a)


test_function([0])
# Pass [0] => [0]
test_function([2, 1])
# Pass [2,1] => [1,2]

test_function([])
# Pass [] => []

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Pass [0,0,2,2,2,1,1,1,2,0,2] => [0,0,0,1,1,1,2,2,2,2,2]

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Pass [2,1,2,0,0,2,1,0,1,0,0,2,2,2,1,2,0,0,0,2,1,0,2,0,0,1] =>
# [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Pass [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2] =>
# [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2]
