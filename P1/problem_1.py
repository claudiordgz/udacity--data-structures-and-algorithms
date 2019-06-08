""" First iteration
Tracking Freshness
"""


def test_lru_cache(class_constructor):
    our_cache = class_constructor(5)
    check = lambda v: "pass" if v is True else "failed"
    result = our_cache.get(1)   # returns -1
    expected = -1
    print(result, expected, check(result == expected))

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(4, 1)
    our_cache.set(10, 2)

    result = our_cache.get(1)   # returns 1
    expected = 1
    print(result, expected, check(result == expected))
    result = our_cache.get(2)   # returns 2
    expected = 2
    print(result, expected, check(result == expected))
    result = our_cache.get(3)   # returns -1
    expected = -1
    print(result, expected, check(result == expected))

    our_cache.set(30, 2)
    our_cache.set(48, 2)
    result = our_cache.get(4)   # returns -1
    expected = -1
    print(result, expected, check(result == expected))

    for i in range(0, 10000):
        our_cache.set(i, i)

    for i in range(0, 10000):
        our_cache.get(i)

    result = our_cache.get(9999)   # returns 495
    expected = 9999
    print(result, expected, check(result == expected))


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.fresh_index = 0
        self.cache = {}
        self.freshness = {}
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        
        self.freshness[key] = self.fresh_index
        self.fresh_index += 1
        return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.capacity:
            self._handle_capacity_max()
        
        self.cache[key] = value
        self.freshness[key] = self.fresh_index
        self.fresh_index += 1

    def _handle_capacity_max(self):
        old_fresh = lambda k: self.freshness[k]
        oldest = min(self.freshness.keys(), key=old_fresh)
        self.cache.pop(oldest)
        self.freshness.pop(oldest)


test_lru_cache(LRU_Cache)
# -1 -1 pass
# 1 1 pass
# 2 2 pass
# -1 -1 pass
# -1 -1 pass
# 9999 9999 pass


""" Second Iteration
Custom HashMap
"""


class DoubleNode:
    
    def __init__(self):
        self.value = None
        self.next = None
        self.previous = None


"""
The OrderedDict needs to know the order that we inserted our elements, it only receives a key

To do this:
We keep a Double Linked List of all nodes
We keep a table of all the (key, Node) in list
When pushing:
    if a key is already in table:
        remove and add at the end
    else:
        add at the end
When pop:
    return head key and move head to next

We must keep track of size and tail to have O(1) operations
"""


class OrderedDict:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        self.nodes = {}

    def add(self, key):
        try:
            node = self.nodes[key]
            if node.previous is None:
                self.head = node.next
                self.head.previous = None
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
                self.nodes[key] = node
                node.next = None
            else:
                previous = node.previous
                nxt = node.next
                previous.next = nxt
                nxt.previous = previous
                node.previous = self.tail
                self.tail = node
                self.nodes[key] = node
                node.next = None
        except:
            node = DoubleNode()
            node.value = key
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                if self.tail.previous is None:
                    self.head.next = node
                    node.previous = self.head
                    self.tail = node
                else:
                    self.tail.next = node
                    node.previous = self.tail
                    self.tail = node
            self.nodes[key] = node
            self.num_elements += 1
  
    def pop(self):
        if self.is_empty():
            return None

        head = self.head
        key = head.value
        self.head = head.next
        self.head.previous = None
        self.nodes.pop(key)
        self.num_elements -= 1
        return key

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _print(self):
        if self.head is None:
            return []
        itr = self.head
        l = []
        while itr:
            l.append(str(itr.value))
            itr = itr.next
        return ",".join(l)

    def __repr__(self):
        return self._print()

    def __str__(self):
        return self._print()


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.order = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1

        self.order.add(key)
        return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.capacity:
            self._handle_capacity_max()
        
        self.cache[key] = value
        self.order.add(key)

    def _handle_capacity_max(self):
        key = self.order.pop()
        self.cache.pop(key)


test_lru_cache(LRU_Cache)
# -1 -1 pass
# 1 1 pass
# 2 2 pass
# -1 -1 pass
# -1 -1 pass
# 9999 9999 pass

"""collections.OrderedDict
"""
import collections


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


test_lru_cache(LRU_Cache)
# -1 -1 pass
# 1 1 pass
# 2 2 pass
# -1 -1 pass
# -1 -1 pass
# 9999 9999 pass
