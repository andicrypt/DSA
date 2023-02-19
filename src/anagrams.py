# tag: [trie]

# print anagrams from wordlist
# input: ["listen", "silent", "triangle", "integral"]
# output: [("listen", "silent"), ("triangle", "integral")]

from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.words = []


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        key = ''.join(sorted(word))
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.words.append(word)

    def find_anagrams(self) -> List[tuple[str, str]]:
        anagrams = []
        stack = [self.root]

        while stack:
            node = stack.pop()

            for child_node in node.children.values():
                if len(child_node.words) > 1:
                    for i in range(len(child_node.words)):
                        for j in range(i+1, len(child_node.words)):
                            anagrams.append(
                                (child_node.words[i], child_node.words[j]))
                stack.append(child_node)

        return anagrams


trie = Trie()
words = ["listen", "silent", "triangle", "integral"]
for word in words:
    trie.insert(word)

print(trie.find_anagrams())
