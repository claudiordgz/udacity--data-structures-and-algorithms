import hashlib
import datetime
import json


class Block:

    def __init__(self, index, timestamp, data, previous_hash=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = "starting block" if previous_hash is None else previous_hash
        self.hash = self.calc_hash(self.previous_hash)

    def get_index(self):
        return self.index

    def get_previous_hash(self):
        return self.previous_hash

    def get_hash(self):
        return self.hash

    def calc_hash(self, previous_hash):
        sha = hashlib.sha256()
        hash_str = str(previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def _print(self):
        rep = {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }
        return json.dumps(rep)

    def __str__(self):
        return self._print()

    def __repr__(self):
        return self._print()


class Blockchain:

    def __init__(self):
        self.num_elements = 0
        self.tail = None
        self.nodes = {}

    def _get_timestamp(self):
        return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def add(self, value):
        timestamp = self._get_timestamp()
        if self.tail is None:
            self.tail = Block(self.num_elements, timestamp, value, None)
            self.nodes[self.tail.get_hash()] = self.tail
            self.num_elements += 1
        else:
            node = Block(self.num_elements, timestamp, value, self.tail.get_hash())
            self.tail = node
            self.nodes[self.tail.get_hash()] = self.tail
            self.num_elements += 1

    def _print(self):
        itr = self.tail
        l = []
        while itr:
            string = "Hash {}: {}".format(itr.get_index(), str(itr))
            l.append(string)
            try:
                itr = self.nodes[itr.get_previous_hash()]
            except KeyError:
                break
        return "\n".join(l)

    def __str__(self):
        return self._print()

    def __repr__(self):
        return self._print()


def test_case():
    chain = Blockchain()
    chain.add("I'm walking on sunshine")
    chain.add("I just bought a boat")
    chain.add("I sold these for debts")
    chain.add("Need a new lambo")
    print(chain)
    # Hash 3: {"index": 3, "timestamp": "2019-06-08T16:20:40.235565UTC", "data": "Need a new lambo", "previous_hash": "2ae9320b6e1b4c36bce58c4dd8a844a25d588006c0aafe446a55ec10470d504f"}
    # Hash 2: {"index": 2, "timestamp": "2019-06-08T16:20:40.235543UTC", "data": "I sold these for debts", "previous_hash": "a0831bb6fe72426dac173f51dd6cc5e30d380fd781dcfd862d2fc71d5fde173a"}
    # Hash 1: {"index": 1, "timestamp": "2019-06-08T16:20:40.235514UTC", "data": "I just bought a boat", "previous_hash": "773766b937f82830ec3acd0269686449dc28901940f2b18bcd316d1fdb5639f9"}
    # Hash 0: {"index": 0, "timestamp": "2019-06-08T16:20:40.235371UTC", "data": "I'm walking on sunshine", "previous_hash": "starting block"}


def test_case_2():
    chain = Blockchain()
    print(chain)
    #


def test_case_3():
    chain = Blockchain()
    for i in range(100):
        chain.add("node {}".format(i))
    print(chain)
# Hash 99: {"index": 99, "timestamp": "2019-06-08T16:22:52.759622UTC", "data": "node 99", "previous_hash": "c3e04d3ace67a8a040801f5c71a4078ee091b82704a1ae6b8f1cd6fba755573a"}
# Hash 98: {"index": 98, "timestamp": "2019-06-08T16:22:52.759614UTC", "data": "node 98", "previous_hash": "a5e8c81789e53be2ae079b9b568d23d39ea2a9bb1cac292f18f6ac0a463ed158"}
# Hash 97: {"index": 97, "timestamp": "2019-06-08T16:22:52.759605UTC", "data": "node 97", "previous_hash": "5f3ccebe35f162e3e99c1a6736a48cb1910a8553c9466c02db26a8b1160b8bf3"}
# Hash 96: {"index": 96, "timestamp": "2019-06-08T16:22:52.759596UTC", "data": "node 96", "previous_hash": "c859d7d7cb65c89888402f9b1f3539a15468f8d4904e8ae4306a588d7821b007"}
# ...
# Hash 0: {"index": 0, "timestamp": "2019-06-08T16:22:52.758455UTC", "data": "node 0", "previous_hash": "starting block"}


test_case()
test_case_2()
test_case_3()
