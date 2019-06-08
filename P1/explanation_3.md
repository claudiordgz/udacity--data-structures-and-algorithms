# Huffman Coding

This one was very challenging and overwhelming. For the longest of time, I didn't know how to proceed, as if panic took hold of me. I read the Wikipedia page over and over again, trying to understand what I was supposed to do. It felt like too many steps, too inefficient. It took me so long to figure out that from the tree, I would retrieve the codes for each character.

## Encoding

The first thing I did is doing the steps with sentences, building the tree on paper, it looked like some queue, but it had to keep order. I would be inserting elements into the queue as I was building the tree. I started looking into min heaps since I heard about them before, and then quickly found out that if you insert one with a tuple of `(frequency, node),` then you can have the Priority Queue ready for action. The computational complexity of the min heap was exciting because it is `O(log(n))` and popping the correct elements is `O(1)`, but the real reason I wanted it is because it was the one that made the most sense when I was building the tree on paper.

There was only one problem with this approach. I did not want to save the frequency on the node, because it was already on the queue. But if there were two elements with the same frequency, `heappush` would try to compare the next item, which was the node. I quickly found that you can do `(frequency, counter, node)` and the counter a number that always increases. This approach was also very similar to my on paper algorithm.

The complexity for construction is `O((n)log(n))`.

## Decoding

But now I had another problem, is my tree correct? I copied the print tree function we implemented on the lessons and verified it was ok. And for the codes, I used a map that would have the char mapping to a binary string such as `0001`. Coding the data with this table was trivial. I navigated `O(k)` elements in the tree to retrieve each code, where `k` is the subset of `n`, and worst case is `k == n`.

Decoding was similarly straightforward, I had some trouble iterating the tree correctly, but thanks to some debugging, I was able to find out that I was navigating incorrectly. I was delighted with the algorithm because decoding is `O(m)` where `m` is the length of the encoded message.

## Conclusion

Encoding is very useful, but if we could encode and end of word character (say `\t`), then we can use a bi directional Hash Table to decode the encoded data. 
