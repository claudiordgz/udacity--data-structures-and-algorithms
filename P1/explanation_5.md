# Blockchain

We will go ahead and create a blockchain, which seems to be a singly linked list. In order to hash the previous block first we need to make a representation of it, we will use a dictionary for that. In Python, a dictionary can be represented in a JSON form using the json dependency, which will allow us to Hash it for our next block. We will use a HashTable of every hash as our main ledger.

Complexity is very high level when it comes to this problem. We add `O(1)` on time and space, but we would still need to look into making the code robust for transactions over the network.
