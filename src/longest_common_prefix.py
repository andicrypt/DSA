# tag: [trie]

# problem finding the longest prefix
# input: ['flower', 'flow', 'flight']
# output: 'fl'

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.nword = 0

    def insert(self, word: str) -> None:
        self.nword += 1
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def longest_common_prefix(self) -> str:
        node = self.root
        prefix = ""
        while len(node.children) == 1 and node.count <= self.nword:
            char, child_node = next(iter(node.children.items()))
            prefix += char
            node = child_node
        print(prefix)
        return prefix


words = ['flower', 'flow', 'flight']

trie = Trie()
for word in words:
    trie.insert(word)

print(trie.longest_common_prefix())
