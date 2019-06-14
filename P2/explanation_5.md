# Solution

I used a recursive solution to find all child possibilities. For every single `iterator` or Node, I call the same function that will go and collect all children of that node. 

I also do an iteration on the `find` function, because this allows me to handle a larger prefix such as `ant`. 

We could say it is `O(n - h)` where `h` is the levels down we navigated in the tree, but it does not make a difference. Thus the Complexity is `O(n)` where n is the size of the trie.
