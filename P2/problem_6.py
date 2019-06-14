import random
import sys

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    _max = -sys.maxsize -1
    _min = sys.maxsize

    for i in ints:
        if i > _max:
            _max = i
        if i < _min:
            _min = i
    
    return (_min, _max)


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Pass

l = [i for i in range(0, 2)]
random.shuffle(l)
print("Pass" if ((0, 1) == get_min_max(l)) else "Fail")
# Pass

l = [i for i in range(10, 1512)]
random.shuffle(l)
print("Pass" if ((10, 1511) == get_min_max(l)) else "Fail")
# Pass

l = [i for i in range(-31551351, 106489716)]
random.shuffle(l)
print("Pass" if ((-31551351, 106489715) == get_min_max(l)) else "Fail")
# Pass
