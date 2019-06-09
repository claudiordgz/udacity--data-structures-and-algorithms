# Least Recently Used Cache

## First iteration

We need to keep track of the "freshness" of every operation.  We can also use a Python Dictionary to store the items instead of building our custom Hash Table. 

To track the freshness, we can use another dictionary, with the key being the same key to cache and the value the freshness index, which is another variable.

## Second iteration

When we search for the `min` we are breaking the rule of *All operations must take `O(1)` time*. One way to handle this could be with a Priority Queue, but then inserting the item would *not* be `O(1)`. Another way to handle it would be to implement our own Hash Table that can handle ordering.

## Conclusion

It is very important not to do any form of looping in our `OrderedDict`.

Right now we keep two dictionaries, one for the order and another for the cache. We can extend our `OrderedDict` to also track the value. There is a collection we could use already in Python doing `from collections import OrderedDict`. Using `OrderedDict` is good practice and supports regular `Dictionary` operations. These optimizations reduce our space complexity worst case to `O(capacity)` and our operation's time complexity to `O(1)`.
