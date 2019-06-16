"""
Calculate the floored square root of a number

Args:
   number(int): Number to find the floored squared root
Returns:
   int: Floored Square Root
"""
import timeit


def sqrt_multiplication(number):

    start = 0
    end = number

    while start <= end:
        midpoint = (start + end) // 2
        ans_1 = midpoint * midpoint
        ans_2 = (midpoint + 1) * (midpoint + 1)
        if ans_1 == number or (ans_1 <= number < ans_2):
            return midpoint
        elif ans_1 < number:
            start = midpoint + 1
        else:
            end = midpoint - 1
    return -1


def sqrt_division(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    start = 0
    end = number

    while start <= end:
        midpoint = (start + end) // 2
        ans_1 = number // midpoint
        if ans_1 == midpoint:
            return midpoint
        elif ans_1 > midpoint:
            start = midpoint + 1
        else:
            end = midpoint - 1
    return -1


def sqrt(n):
    return sqrt_division(n)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

"""
EXTRA TEST CASES
"""
def test_case(fn):
    print("Testing {}".format(fn.__name__))
    ans = fn(9)
    print("Pass" if (3 == ans) else "Fail", "input:", 9, "answer: ", ans)
    ans = fn(0)
    print("Pass" if (0 == ans) else "Fail", "input:", 0, "answer: ", ans)
    ans = fn(16)
    print("Pass" if (4 == ans) else "Fail", "input:", 16, "answer: ", ans)
    ans = fn(1)
    print("Pass" if (1 == ans) else "Fail", "input:", 1, "answer: ", ans)
    ans = fn(27)
    print("Pass" if (5 == ans) else "Fail", "input:", 27, "answer: ", ans)
    ans = fn(32153)
    print("Pass" if (179 == ans) else "Fail", "input:", 32153, "answer: ", ans)
    ans = fn(384383846843438646)
    print(
        "Pass" if (
            619986973 == ans) else "Fail",
        "input:",
        384383846843438646,
        "answer: ",
        ans)


test_case(sqrt_multiplication)
# Testing sqrt_multiplication
# Pass input: 9 answer:  3
# Pass input: 0 answer:  0
# Pass input: 16 answer:  4
# Pass input: 1 answer:  1
# Pass input: 27 answer:  5
# Pass input: 32153 answer:  179
# Pass input: 384383846843438646 answer:  619986973
test_case(sqrt_division)
# Testing sqrt_division
# Pass input: 9 answer:  3
# Pass input: 0 answer:  0
# Pass input: 16 answer:  4
# Pass input: 1 answer:  1
# Pass input: 27 answer:  5
# Pass input: 32153 answer:  179
# Pass input: 384383846843438646 answer:  619986973


def test_multiplication():
    return sqrt_multiplication(384383846843438646)


def test_division():
    return sqrt_division(384383846843438646)
