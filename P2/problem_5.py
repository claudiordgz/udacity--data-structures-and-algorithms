# # Building a Trie in Python
#
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# Give it a try by implementing the `TrieNode` and `Trie` classes below!
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def insert(self, char):
        # Add a child node in this Trie
        return self.children[char]

    def has_children(self, char):
        return char in self.children

    def get_child(self, char):
        return self.children[char] if char in self.children else None

    def set_word(self):
        self.is_word = True

    def _suffixes(self, node, s_list, suffix=''):
        for char in node.children:
            s = "{}{}".format(suffix, char)
            self._suffixes(node.get_child(char), s_list, s)
        if node.is_word:
            s_list.append(suffix)

    def suffixes(self):
        # Recursive function that collects the suffix for
        # all complete words below this point
        s = []
        self._suffixes(self, s)
        return s


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        itr = self.root
        for char in word:
            itr = itr.insert(char)
        itr.set_word()

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        itr = self.root
        for char in prefix:
            itr = itr.get_child(char)
        return itr


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def test_case(trie):
    node = trie.find("a")
    suffixes = node.suffixes()
    print(
        'is correct for a? ',
        suffixes == [
            'nthology',
            'ntagonist',
            'ntonym',
            'nt'],
        suffixes)
    node = trie.find('f')
    suffixes = node.suffixes()
    print(
        'is correct for f? ',
        suffixes == [
            'unction',
            'un',
            'actory'],
        suffixes)


def test_case_longer(trie):
    node = trie.find("tri")
    suffixes = node.suffixes()
    print(
        'is correct for tri? ',
        suffixes == [
            'e',
            'gger',
            'gonometry',
            'pod'],
        suffixes)
    node = trie.find('ant')
    suffixes = node.suffixes()
    print(
        'is correct for ant? ',
        suffixes == [
            'hology',
            'agonist',
            'onym',
            ''],
        suffixes)


def test_case_invalid(trie):
    node = trie.find("c")
    print('is c None? ', node is None)


test_case(MyTrie)
# is correct for a?  True ['nthology', 'ntagonist', 'ntonym', 'nt']
# is correct for f?  True ['unction', 'un', 'actory']

test_case_longer(MyTrie)
# is correct for tri?  True ['e', 'gger', 'gonometry', 'pod']
# is correct for ant?  True ['hology', 'agonist', 'onym', '']

test_case_invalid(MyTrie)
# is c None?  True
