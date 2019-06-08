import sys
import heapq
from collections import defaultdict, deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.num_elements = 0

    def push(self, value):
        heapq.heappush(self.heap, value)
        self.num_elements += 1

    def pop(self):
        node = heapq.heappop(self.heap)
        self.num_elements -= 1
        return node

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def _get_text(self):
        return f"♠{self.get_value()}" if self.get_value() is not None else " -"

    def __repr__(self):
        return f"{self._get_text()}"

    def __str__(self):
        return f"{self._get_text()}"

    def is_leaf(self):
        return self.value is not None and self.left is None and self.right is None


def calculate_frequencies(data):
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1
    p_queue = PriorityQueue()
    for i, (k, v) in enumerate(frequencies.items()):
        p_queue.push((v, i, Node(k)))
    return p_queue


class HuffmanTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_root(self):
        return self.root

    def set_root(self, value):
        self.root = value

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while(len(q) > 0):
            node, level = q.deq()
            if node is None:
                visit_order.append(("  ", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


def __make_encoding(node, codes, code=""):
    if node is None:
        return None
    left = node.get_left_child()
    right = node.get_right_child()
    if left.is_leaf():
        codes[left.get_value()] = code + "0"
    else:
        new_code = code + "0"
        __make_encoding(left, codes, new_code)
    if right.is_leaf():
        codes[right.get_value()] = code + "1"
    else:
        new_code = code + "1"
        __make_encoding(right, codes, new_code)


def make_encoding_map(huffman_tree):
    codes = dict()
    __make_encoding(huffman_tree.get_root(), codes)
    return codes


def build_huffman_tree(frequencies):
    hf_tree = HuffmanTree()
    count = frequencies.size() + 1
    root = None
    while not frequencies.is_empty():
        try:
            f_freq, _, f_node = frequencies.pop()
            s_freq, _, s_node = frequencies.pop()
            root = Node()
            root.left = f_node
            root.right = s_node
            frequencies.push((f_freq + s_freq, count, root))
            count += 1
        except IndexError:
            hf_tree.set_root(root)
    return hf_tree


def encode_data(codex, data):
    s = ""
    for char in data:
        s += codex[char]
    return s


def huffman_encoding(data, debug=False):
    if not data:
        return None, None
    frequencies = calculate_frequencies(data)
    tree = build_huffman_tree(frequencies)
    codex = make_encoding_map(tree)
    if debug:
        print(tree)
        print(codex)
    encoded_data = encode_data(codex, data)
    return encoded_data, tree


def __navigate(char, node):
    if char == "0":
        return node.get_left_child()
    else:
        return node.get_right_child()


def huffman_decoding(data, tree):
    decoded = ""
    node = tree.get_root()
    for char in data:
        if node.is_leaf():
            decoded += node.get_value()
            node = __navigate(char, tree.get_root())
        else:
            node = __navigate(char, node)
    if node.is_leaf():
        decoded += node.get_value()
    return decoded


def test_huffman(word):
    print("--------------- TEST ---------------")
    a_great_sentence = word

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    if encoded_data is not None:
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    test_huffman("The bird is the word")
    # --------------- TEST ---------------
    # The size of the data is: 69
    #
    # The content of the data is: The bird is the word
    #
    # The size of the encoded data is: 36
    #
    # The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010
    #
    # The size of the decoded data is: 69
    #
    # The content of the encoded data is: The bird is the word
    test_huffman("")
    # --------------- TEST ---------------
    # The size of the data is: 49
    #
    # The content of the data is:
    test_huffman("hello world")
    # --------------- TEST ---------------
    # The size of the data is: 60
    #
    # The content of the data is: hello world
    #
    # The size of the encoded data is: 32
    #
    # The content of the encoded data is: 11101111101011000000111001010011
    #
    # The size of the decoded data is: 60
    #
    # The content of the encoded data is: hello world
    test_huffman("15683541343")
    # --------------- TEST ---------------
    # The size of the data is: 60
    #
    # The content of the data is: 15683541343
    #
    # The size of the encoded data is: 28
    #
    # The content of the encoded data is: 1101110100111011100110100010
    #
    # The size of the decoded data is: 60
    #
    # The content of the encoded data is: 15683541343
