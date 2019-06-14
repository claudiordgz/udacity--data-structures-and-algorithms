Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:

## Solution

To obtain `O(log(n))` the only viable solution is binary search. Because of the shift in the array, we need to find the pivot index first. If we do both operations using Binary Search, then we won't be breaking the rule. 

Finding the Pivot requires us to keep track of the first element in the array; we also need to keep track of the last minimum item found. Using this technique, we find the pivot index and return it to perform the second step.

The second step is also Binary Search, but we will use the pivot index to offset our midpoint.

Our space is constant since it's keeping track of a specified amount of variables, and doing both binary searches makes sure the complexity does not go above `O(log(n))`.
