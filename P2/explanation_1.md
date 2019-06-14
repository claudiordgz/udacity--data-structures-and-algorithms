# Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is `O(log(n))`

Here is some boilerplate code and test cases to start with:

# Solution

My first iteration was to get an answer, so I did a linear search, keeping track of the previous and the current. This solution ran in `O(n)` where n was the input integer.

Since the expected answer needs to be `O(log(n))` that helps find the answer faster. A right choice would be to use Binary Search since we are searching in all elements sorted from 0 to the input integer. 

The main thing we need to watch out for is the decimals. In my first solution, I was doing `i * i` for every single possible answer between `0-n`.

To account for decimals, we have to check both the `midpoint` and `midpoint + 1`.

Alternatively, we could divide the number by the midpoint. Using Python's truncate division, we should be able to obtain the exact amount.  This micro performance saves us some checks in our loop. 

Using `timeit` to measure runtime we can get consistent running times in seconds for each function: 

```
for n=384383846843438646
multiplication: 21.016345699999874
division: 16.180409100000134
```
 