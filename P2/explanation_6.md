# Max and Min in a Unsorted Array

In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?

Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm (i.e., linear time)?

# Solution

Searching for min and max in an unsorted array can be done in `O(n)` time. To do it, we keep track of two variables, min, and max, and we set max to a minimum value and min to a massive one. 

We traverse the array one time, checking each number to see if it's larger than max, or smaller than min. 
