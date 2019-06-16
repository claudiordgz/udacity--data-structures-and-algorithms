# Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

# Solution

My first instinct was to implement this by keeping a count of 0, 1, and 2, then creating a list using those counts. The problem with this approach is that creating the list could be a second iteration, breaking the rule of `using a single traversal`. 

The second approach would be to iterate the array using three-pointers, one to keep track of the positions with zero at the beginning, another for locations with two at the end, and another to navigate the array. 

This approach checks each number in the array once in a single loop. 
