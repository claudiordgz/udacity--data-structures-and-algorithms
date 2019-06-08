# Union and Intersection of Two Linked Lists

## Union

> The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. 

The union is every element in both A and B. Without using the built-in set collection; we could build a Dictionary with every element. The Time Complexity would be `O(n + m)` where **n** is the elements in A, and **m** is the elements in B. Then we assemble our LinkedList using all the keys. The Space Complexity is also `O(n + m)` which would be for all elements in both lists to be different.

## Intersection

> The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

The union is every element in both A and B. Without using the built-in set collection; we could build a Dictionary with every element. The Time Complexity would be `O(n + m)` where **n** is the elements in A, and **m** is the elements in B. Then we assemble our LinkedList checking that the elements of one dictionary are in the other one. The Space Complexity is also `O(n + m)` which would be for all elements in both lists to be different.

I tried finding literature to getting something better than `O(n)` to no avail. Using the Hash Table, which also seems what `Set` is using under the hood, is a reasonable solution.
